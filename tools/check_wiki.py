"""Contrôles statiques du wiki, sans dépendance externe ni lancement de Minecraft."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import base64
import struct
import sys
import xml.etree.ElementTree as ET
import zlib

ROOT = Path(__file__).resolve().parents[1] / "site"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError(f"Identifiant répété : {self.path}: {attrs['id']}")
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "img" and "alt" not in attrs:
            print(f"AVERTISSEMENT : image sans alt dans {self.path.relative_to(ROOT)}")


def verify_png(raw, source):
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Signature PNG incorrecte : {source}")
    pos = 8
    compressed = bytearray()
    ended = False
    while pos < len(raw):
        if pos + 12 > len(raw):
            raise ValueError(f"PNG tronqué : {source}")
        count = struct.unpack_from(">I", raw, pos)[0]
        end = pos + 12 + count
        if end > len(raw):
            raise ValueError(f"Bloc PNG tronqué : {source}")
        kind = raw[pos + 4:pos + 8]
        payload = raw[pos + 8:pos + 8 + count]
        expected = struct.unpack_from(">I", raw, pos + 8 + count)[0]
        if zlib.crc32(kind + payload) & 0xffffffff != expected:
            raise ValueError(f"CRC PNG incorrect : {source}, {kind!r}")
        if kind == b"IDAT":
            compressed.extend(payload)
        pos = end
        if kind == b"IEND":
            ended = True
            break
    if not ended or pos != len(raw) or not compressed:
        raise ValueError(f"Structure PNG incorrecte : {source}")
    zlib.decompress(bytes(compressed))


def main():
    pages = {path.resolve(): Page(path) for path in ROOT.rglob("*.html")}
    if not pages:
        raise ValueError("Aucune page HTML trouvée")
    links = 0
    for path, page in pages.items():
        for link in page.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            if parts.path.startswith("/"):
                raise ValueError(f"Lien absolu non portable sur Pages : {path}: {link}")
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if target.is_dir():
                target = target / "index.html"
            if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
                raise ValueError(f"Lien local manquant : {path.relative_to(ROOT)}: {link}")
            if parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                raise ValueError(f"Ancre manquante : {path.relative_to(ROOT)}: {link}")
            links += 1
    svg_count = 0
    png_count = 0
    for path in ROOT.rglob("*.svg"):
        tree = ET.parse(path)
        svg_count += 1
        for element in tree.iter():
            for attr, value in element.attrib.items():
                if not attr.endswith("href") or not value.startswith("data:image/png;base64,"):
                    continue
                encoded = "".join(value.split(",", 1)[1].split())
                raw = base64.b64decode(encoded, validate=True)
                verify_png(raw, path.relative_to(ROOT))
                png_count += 1
    print(f"OK : {len(pages)} pages HTML ; {links} liens locaux et ancres ; {svg_count} SVG ; {png_count} PNG intégrés.")
    print("Non vérifiés ici : URLs externes, rendu dans un navigateur, comportement du mod en jeu et activation de GitHub Pages.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, ET.ParseError, zlib.error, struct.error) as exc:
        print(f"ERREUR : {exc}", file=sys.stderr)
        sys.exit(1)
