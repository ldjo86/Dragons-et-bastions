"""Reconstruction déterministe du wiki depuis les recettes et ressources vérifiées."""
from pathlib import Path
from collections import Counter
from html import escape
import hashlib, json, re
from PIL import Image
from wiki_render import Assets, recipe_image
from wiki_content import NAMES, USES, GROUPS, SMITHING_BASE, HEART_NOTE, SCALE_NOTE

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
OUT=SITE/'generated'
RECIPES=json.loads((ROOT/'tools/recipes.json').read_text(encoding='utf-8'))
VANILLA={
'string':'Ficelle','iron_ingot':'Lingot de fer','iron_nugget':'Pépite de fer','gold_ingot':"Lingot d’or",
'diamond':'Diamant','netherite_ingot':'Lingot de netherite','stick':'Bâton','feather':'Plume',
'crossbow':'Arbalète','bow':'Arc','leather':'Cuir','chest':'Coffre','emerald':'Émeraude',
'map':'Carte vierge','smooth_stone':'Pierre lisse','stone_slab':'Dalle de pierre',
'fletching_table':"Table d’archerie",'obsidian':'Obsidienne','blaze_powder':'Poudre de Blaze',
'nether_brick':'Brique du Nether','echo_shard':"Éclat d’écho",'diamond_helmet':'Casque en diamant',
'diamond_chestplate':'Plastron en diamant','diamond_leggings':'Jambières en diamant',
'diamond_boots':'Bottes en diamant','diamond_sword':'Épée en diamant'}

def name(item):
    if not item:return 'Case vide'
    if item=='#minecraft:planks':return 'Planches acceptées par #minecraft:planks'
    if item=='#minecraft:logs':return 'Bûche acceptée par #minecraft:logs'
    ns,key=item.split(':',1)
    if ns=='ballista':return NAMES[key]
    return VANILLA.get(key,key.replace('_',' '))

def recipe_data(key,r):
    kind=r['type'];smith=kind.startswith('ballista:');loose=kind.endswith('crafting_shapeless')
    if smith:
        base=SMITHING_BASE[r['base']]
        addition=r.get('addition','ballista:dragon_heart')
        return [None,base,addition],base,1,True,False
    if loose:
        slots=r['ingredients']+[None]*(9-len(r['ingredients']))
    else:
        pattern=r['pattern']+['   ']*(3-len(r['pattern']))
        slots=[r['key'].get(c) for line in pattern for c in line.ljust(3)]
    return slots,r['result']['id'],r['result'].get('count',1),False,loose

def main():
    assert len(RECIPES)==29
    order=[key for _,_,keys in GROUPS for key in keys]
    assert len(order)==29 and set(order)==set(RECIPES)
    (OUT/'crafts').mkdir(parents=True,exist_ok=True)
    (OUT/'icons').mkdir(parents=True,exist_ok=True)
    assets=Assets()
    sections=[];report={'source':'ballista-fabric-0.27.1+mc26.2.jar','sha256':'e85ac8a4a68c773b2ab5b81c1dc7eedad2b6eee91028ebd29d8c68ab1c245b55','recipes':[],'icons':[],'tests':'Ressources et rendu statique ; pas de lancement de Minecraft.'}
    for group,title,keys in GROUPS:
        cards=[]
        for key in keys:
            r=RECIPES[key];slots,result,count,smith,loose=recipe_data(key,r)
            im=recipe_image(assets,slots,result,count,smith,loose)
            target=OUT/'crafts'/f'{key}.png';im.save(target,optimize=True)
            with Image.open(target) as check:check.verify()
            basekey=result.split(':')[1]
            if smith:
                label='Infuser un équipement avec un cœur' if key=='dragon_heart' else 'Appliquer : '+NAMES[r['addition'].split(':')[1]].lower()
                use=HEART_NOTE if key=='dragon_heart' else SCALE_NOTE
            else:
                label=('Réparer : ' if key.startswith('repair_') else '')+NAMES[basekey]
                use=USES[basekey]
            ingredients=Counter(i for i in slots if i)
            materials=' + '.join(f'{n} × {name(item)}' for item,n in ingredients.items())
            note='Table de forge · modèle vide' if smith else ('Table de craft · sans forme' if loose else 'Table de craft · motif 3 × 3')
            alt=label+'. '+('Modèle vide ; '+materials if smith else 'Cases : '+' / '.join(name(i) for i in slots))+f'. Résultat : {count} × {name(result)}'+(' amélioré' if smith else '')+'.'
            image=f'generated/crafts/{key}.png'
            tag_note='<p class="small">Le chêne illustré est un exemple : tout ingrédient admis par le tag indiqué convient.</p>' if any(i and i.startswith('#') for i in slots) else ''
            cards.append(f'<article class="recipe searchable" id="craft-{key}"><p class="kicker">{escape(note)}</p><h3>{escape(label)}</h3><a href="{image}" target="_blank" rel="noopener" aria-label="Agrandir : {escape(label)}"><img src="{image}" alt="{escape(alt)}" width="560" height="300" loading="lazy"></a><div class="recipe-text"><p class="materials"><b>Ingrédients :</b> {escape(materials)}.</p><p><b>Résultat :</b> {count} × {escape(name(result))}{" amélioré" if smith else ""}.</p><p><b>Utilité et utilisation :</b> {escape(use)}</p>{tag_note}</div></article>')
            report['recipes'].append({'id':key,'type':r['type'],'image':image,'slots':slots,'result':result,'count':count,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
            print('CRAFT OK',key,flush=True)
        sections.append(f'<section class="recipe-group" id="{group}"><h2>{escape(title)}</h2><div class="recipe-grid">'+''.join(cards)+'</div></section>')
    blocks=['dragon_hunter_table','obsidian_fletching_table','infernal_fletching_table','echo_fletching_table','wooden_spikes','iron_spikes','red_dragon_egg','green_dragon_egg','blue_dragon_egg','light_ballista_wreck','medium_ballista_wreck','heavy_ballista_wreck']
    items=[key.split('/')[-1] for key in assets.data['textures'] if key.startswith('ballista:item/')]
    catalogue=[]
    for category,keys in [('Objets et équipement',items),('Blocs à poser et à récupérer',blocks)]:
        cards=[]
        for key in keys:
            ref='ballista:'+key
            target=OUT/'icons'/f'{key}.png';assets.icon(ref).save(target,optimize=True)
            image='generated/icons/'+key+'.png'
            owncraft=next((rid for rid,r in RECIPES.items() if r.get('result',{}).get('id')==ref and not rid.startswith('repair_')),None)
            obtaining=f'<a href="#craft-{owncraft}">Voir le craft et son résultat ↑</a>' if owncraft else 'Pas de recette de fabrication déclarée dans ce JAR.'
            cards.append(f'<article class="object searchable" id="objet-{key}"><img src="{image}" width="160" height="160" loading="lazy" alt="{escape(NAMES[key])} : texture ou modèle réel du mod"><div><h3>{escape(NAMES[key])}</h3><p>{escape(USES[key])}</p><p class="obtaining">{obtaining}</p><small><code>{ref}</code></small></div></article>')
            report['icons'].append({'id':ref,'image':image,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
            print('ICONE OK',key,flush=True)
        catalogue.append(f'<h2>{category}</h2><div class="object-grid">'+''.join(cards)+'</div>')
    original=(SITE/'dragons.html').read_text(encoding='utf-8')
    match=re.search(r'<main\b[^>]*>(.*?)</main>',original,re.S)
    if not match:raise ValueError('Guide dragons existant introuvable : ne pas le remplacer par un résumé')
    guide=match.group(1).replace('href="recettes.html"','href="#crafts"').replace('href="index.html"','href="#haut"')
    intro='''<section class="intro" id="crafts"><p class="eyebrow">LE GUIDE COMPLET, DANS L’ORDRE</p><h1>Fabriquer.<br>Défendre.<br>Élever son dragon.</h1><p>Les crafts d’abord, leur résultat et leur utilité juste dessous, puis les objets, les blocs et le parcours de l’œuf à la monture. Tout se lit sur cette page.</p><div class="stats"><span><b>29</b> recettes illustrées</span><span><b>24 + 5</b> crafts et améliorations à la forge</span><span><b>26.2</b> Minecraft Java · Fabric</span></div><aside class="notice">Les icônes proviennent des ressources réelles : aucun ingrédient n’est remplacé par un mot dans une case. Clique sur une image pour l’agrandir. Les recettes sans forme sont signalées ; les améliorations à la forge ont un schéma distinct.</aside><label class="search-label" for="recherche">Retrouver un craft, un objet ou un bloc</label><input type="search" id="recherche" placeholder="Baliste, selle, armure, cœur…"><p class="small" id="recherche-info" aria-live="polite">Le guide d’élevage reste visible pendant la recherche.</p></section>'''
    play='''<section id="utilisation-balistes" class="guide"><p class="eyebrow">APRÈS LES CRAFTS</p><h2>Installer et utiliser ses défenses</h2><p>Une baliste est une entité posée depuis son objet. Dégage son emplacement, puis interagis avec des flèches ou des amorces : la réserve atteint au maximum <b>64 tirs</b>. L’amorce n’est pas un composant inutilisable seul : le code la charge directement.</p><p>Une table d’archerie détectée <b>sous l’emprise ou contre un côté</b> assure le ravitaillement. Les tables spécialisées sélectionnent les tirs obsidienne, infernaux ou des profondeurs. Sans table reconnue, la baliste utilise sa réserve de munitions. Les échanges avec une baliste déjà possédée sont réservés à son propriétaire, hors exceptions créatives du code.</p><p>Pour récupérer sa baliste, son propriétaire utilise l’interaction <b>accroupi, main vide</b>. Le code restitue l’objet et la réserve sous forme de flèches. Une épave doit d’abord être réparée avec sa recette propre.</p><div class="table-scroll"><table><thead><tr><th>Baliste</th><th>Dégâts de base</th><th>Portée</th><th>Rechargement</th></tr></thead><tbody><tr><td>Légère</td><td>8</td><td>12 blocs</td><td>40 ticks</td></tr><tr><td>Moyenne</td><td>14</td><td>14 blocs</td><td>80 ticks</td></tr><tr><td>Lourde</td><td>22</td><td>16 blocs</td><td>40 ticks</td></tr></tbody></table></div><p class="small">Valeurs de BallistaVariant, avant les effets des tirs et les conditions du combat. 40 ticks correspondent à 2 secondes si le serveur tient 20 ticks/s. La baliste moyenne n’est donc pas la plus rapide.</p><h3>Le chasseur de dragons</h3><p>Ce marchand utilise la table de chasse draconique. Ses offres de base comprennent : 2 écailles contre 5 émeraudes, 1 cœur contre 24 émeraudes ; dans l’autre sens, 10 émeraudes pour 2 écailles, 32 pour un cœur, 8 pour un sifflet et 2 pour 8 amorces. Ces prix de base ne garantissent pas un stock illimité ni l’absence de variations.</p><p>La carte d’antre est une carte personnalisée liée à un antre connu de l’index du monde, pas une recette supplémentaire. Les œufs d’apparition ne sont pas les œufs d’incubation obtenus dans les antres.</p></section>'''
    footer='''<section id="installation" class="guide"><h2>Installation et périmètre</h2><p>Cette page documente <b>ballista-fabric-0.27.1+mc26.2.jar</b> (nom du manifeste : Baliste). Le JAR exige Minecraft Java 26.2, Fabric Loader ≥ 0.19.3, Java ≥ 25 et Fabric API. Sauvegarde ton monde avant toute installation ; aucune compatibilité avec une autre version n’est déduite.</p><p>Les explications proviennent des recettes, modèles, textures, tables de butin et classes du JAR. Les images sont des assemblages et rendus hors jeu, pas des captures dans Minecraft. Le JAR et le client Minecraft complets ne sont pas publiés avec le wiki. Les ressources du mod et de Minecraft conservent leurs droits respectifs.</p><p><b>Vérifications :</b> 29 recettes couvertes, ingrédients et quantités enregistrés, ressources contrôlées par empreinte, PNG décodés et liens locaux vérifiés. Aucun lancement de Minecraft n’a été effectué.</p><p class="small">Cette version de la page réunit les crafts et le catalogue visuel ; elle ne prétend pas remplacer un test en jeu de toutes les IA, invasions ou générations du monde. <a href="generated/rapport.json">Consulter le manifeste des images</a>.</p></section>'''
    page='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dragons et bastions — Crafts, objets et élevage des dragons</title><meta name="description" content="Tous les crafts illustrés avec ingrédients et résultat, objets et blocs, puis élevage des dragons : une seule page pour le JAR 0.27.1 Minecraft 26.2."><link rel="stylesheet" href="wiki.css"></head><body id="haut"><a class="skip" href="#crafts">Aller au contenu</a><header class="topbar"><a class="brand" href="#haut">DRAGONS <span>&</span> BASTIONS</a><span class="version">Wiki · 0.27.1</span></header><nav class="toc" aria-label="Sommaire de la page"><a href="#crafts">Crafts</a><a href="#forge-crafts">Forge</a><a href="#catalogue">Objets et blocs</a><a href="#utilisation-balistes">Utilisation</a><a href="#elevage">Élevage du dragon</a><a href="#depannage">Dépannage</a><a href="#installation">Installation</a></nav><main>'''+intro+''.join(sections)+'<section id="catalogue"><p class="eyebrow">RECONNAÎTRE ET UTILISER</p>'+''.join(catalogue)+'</section>'+play+'<section id="elevage" class="guide"><p class="eyebrow">DE L’ŒUF À LA MONTURE</p><h2>Élever son dragon, étape par étape</h2>'+guide+'</section>'+footer+'''</main><footer class="page-footer">Dragons et bastions · Minecraft Java 26.2 · Documentation fondée sur le JAR fourni.</footer><script>const input=document.getElementById('recherche');input.addEventListener('input',()=>{const q=input.value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim();let n=0;document.querySelectorAll('.searchable').forEach(card=>{const text=card.textContent.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();card.hidden=!!q&&!text.includes(q);if(!card.hidden)n++});document.getElementById('recherche-info').textContent=q?n+' fiches correspondent. Efface la recherche pour tout retrouver.':'Le guide d’élevage reste visible pendant la recherche.'});</script></body></html>'''

    # Le wiki est reconstruit sur chaque push : conserver les ajouts 0.27.10
    # dans un fragment source plutôt que de modifier uniquement site/index.html.
    fragment=(ROOT/'tools'/'wiki_02710_fragment.html').read_text(encoding='utf-8')
    anchor='<section id="utilisation-balistes" class="guide">'
    assert anchor in page and '<section id="nouveautes"' in fragment
    page=page.replace(anchor,fragment+anchor,1)
    page=page.replace('Wiki · 0.27.1','Wiki · 0.27.10-candidate',1)
    page=page.replace('Minecraft Java 26.2 · Documentation fondée sur le JAR fourni','Minecraft Java 26.1–26.3 · Guides 0.27.10 et archives 0.27.1',1)
    page=page.replace('pour le JAR 0.27.1 Minecraft 26.2.','pour les versions 0.27.10 (nouveautés) et 0.27.1 (recettes illustrées).',1)
    page=page.replace('<b>26.2</b> Minecraft Java · Fabric','<b>26.1–26.3</b> Minecraft Java · Fabric (candidate)',1)
    page=page.replace('<b>29</b> recettes illustrées','<b>29 + 2</b> recettes : 29 illustrées, 2 forges nouvelles',1)
    page=page.replace('<a href="#elevage">Élevage du dragon</a>','<a href="#nouveautes">Nouveautés 0.27.10</a><a href="#elevage">Élevage du dragon</a>',1)
    page=page.replace('Le guide d’élevage reste visible pendant la recherche.','La recherche filtre les fiches des recettes, objets et nouveautés.',1)
    page=page.replace('<section id="installation" class="guide"><h2>Installation et périmètre</h2>','<section id="installation" class="guide"><h2>Installation et périmètre</h2><aside class="notice">Le chapitre historique ci-dessous concerne le JAR 0.27.1/26.2. Pour la version 0.27.10-candidate, voir <a href="#versions-02710">la compatibilité actuelle (26.1 à 26.3)</a>.</aside>',1)
    assert page.count('id="nouveautes"')==1 and page.count('id="raids-02710"')==1
    (SITE/'index.html').write_text(page,encoding='utf-8')
    assert len(report['recipes'])==29 and len(list((OUT/'crafts').glob('*.png')))==29
    report['crafting_count']=24;report['smithing_count']=5
    (OUT/'rapport.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'OK : page unique, {len(report["recipes"])} images de recettes, {len(report["icons"])} vignettes.',flush=True)

if __name__=='__main__':main()
