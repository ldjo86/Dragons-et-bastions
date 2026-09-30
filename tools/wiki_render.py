"""Rendus statiques depuis les textures et géométries réelles du mod et de Minecraft."""
import base64, hashlib, io, json, math, os, urllib.request, zipfile, zlib
from pathlib import Path
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont

TOOLS = Path(__file__).resolve().parent

def download(url):
    req=urllib.request.Request(url,headers={'User-Agent':'Dragons-et-bastions-wiki/1.0'})
    with urllib.request.urlopen(req,timeout=180) as r:return r.read()

def client_archive():
    override=os.environ.get('MINECRAFT_CLIENT_JAR')
    if override:return zipfile.ZipFile(override)
    cache=TOOLS/'.cache';cache.mkdir(exist_ok=True)
    manifest=json.loads(download('https://piston-meta.mojang.com/mc/game/version_manifest_v2.json'))
    entry=next(v for v in manifest['versions'] if v['id']=='26.2')
    info=json.loads(download(entry['url']));data=info['downloads']['client']
    dest=cache/'minecraft-26.2.jar'
    if not dest.exists() or hashlib.sha1(dest.read_bytes()).hexdigest()!=data['sha1']:
        raw=download(data['url'])
        if hashlib.sha1(raw).hexdigest()!=data['sha1']:raise ValueError('Empreinte du client Minecraft incorrecte')
        dest.write_bytes(raw)
    return zipfile.ZipFile(dest)

class Assets:
    def __init__(self,folder=TOOLS):
        encoded=''.join(''.join(p.read_text().split()) for p in sorted((folder/'mod_assets').glob('*.b64')))
        raw=zlib.decompress(base64.b64decode(encoded,validate=True))
        if hashlib.sha256(raw).hexdigest()!='6143142f9c5cab81098bc1cf46bcaddd5a60f2ec6b6b8a93e03936aa5d5326b6':
            raise ValueError('Ressources du mod altérées')
        self.data=json.loads(raw)
        self.client=client_archive()

    def resource(self,ref,category,ext):
        ns,path=ref.split(':',1) if ':' in ref else ('minecraft',ref)
        return self.client.read(f'assets/{ns}/{category}/{path}.{ext}')

    @lru_cache(None)
    def texture(self,ref):
        raw=base64.b64decode(self.data['textures'][ref]) if ref in self.data['textures'] else self.resource(ref,'textures','png')
        im=Image.open(io.BytesIO(raw)).convert('RGBA')
        if im.height>im.width:im=im.crop((0,0,im.width,im.width))
        return im

    @lru_cache(None)
    def model(self,ref):
        if ref.startswith('builtin/') or ref=='minecraft:builtin/generated':return {}
        m=self.data['models'].get(ref)
        if m is None:m=json.loads(self.resource(ref,'models','json'))
        p=self.model(m['parent']) if m.get('parent') else {}
        return {**p,**m,'textures':{**p.get('textures',{}),**m.get('textures',{})}}

    @lru_cache(None)
    def icon(self,item):
        item={'#minecraft:planks':'minecraft:oak_planks','#minecraft:logs':'minecraft:oak_log'}.get(item,item)
        ns,key=item.split(':');tex=f'{ns}:item/{key}'
        if ns=='ballista' and tex in self.data['textures']:return fit(self.texture(tex),160)
        if item=='minecraft:chest':return self.render(chest_model())
        block=f'{ns}:block/{key}'+('_0' if ns=='ballista' and key.endswith('_dragon_egg') else '')
        if ns=='ballista' and block in self.data['models']:return self.render(self.model(block))
        try:m=self.model(f'{ns}:item/{key}')
        except KeyError:m={}
        if m.get('elements'):return self.render(m)
        layers=m.get('textures',{});layer=layers.get('layer0')
        if layer:
            for _ in range(15):
                if not layer.startswith('#'):break
                layer=layers[layer[1:]]
            return fit(self.texture(layer),160)
        for ref in [tex,f'{ns}:item/{key}_standby']:
            try:return fit(self.texture(ref),160)
            except KeyError:pass
        return self.render(self.model(block))

    def render(self,model,size=160):
        faces=[];points=[]
        for e in model.get('elements',[]):
            x0,y0,z0=e['from'];x1,y1,z1=e['to']
            vertices={
                'east':[(x1,y1,z0),(x1,y1,z1),(x1,y0,z1),(x1,y0,z0)],
                'west':[(x0,y1,z1),(x0,y1,z0),(x0,y0,z0),(x0,y0,z1)],
                'south':[(x1,y1,z1),(x0,y1,z1),(x0,y0,z1),(x1,y0,z1)],
                'north':[(x0,y1,z0),(x1,y1,z0),(x1,y0,z0),(x0,y0,z0)],
                'up':[(x0,y1,z0),(x0,y1,z1),(x1,y1,z1),(x1,y1,z0)],
                'down':[(x0,y0,z1),(x0,y0,z0),(x1,y0,z0),(x1,y0,z1)]}
            default_uv={'down':[x0,16-z1,x1,16-z0],'up':[x0,z0,x1,z1],
                'north':[16-x1,16-y1,16-x0,16-y0],'south':[x0,16-y1,x1,16-y0],
                'west':[z0,16-y1,z1,16-y0],'east':[16-z1,16-y1,16-z0,16-y0]}
            for side,face in e['faces'].items():
                p=np.array(vertices[side],dtype=float)
                if e.get('rotation'):
                    r=e['rotation'];axis='xyz'.index(r['axis']);angle=math.radians(r['angle'])
                    origin=np.array(r['origin']);p-=origin
                    if r.get('rescale'):p[:,[i for i in range(3) if i!=axis]]/=math.cos(angle)
                    c,s=math.cos(angle),math.sin(angle)
                    matrix=[[[1,0,0],[0,c,-s],[0,s,c]],[[c,0,s],[0,1,0],[-s,0,c]],[[c,-s,0],[s,c,0],[0,0,1]]][axis]
                    p=p@np.array(matrix).T+origin
                normal=np.cross(p[1]-p[0],p[2]-p[0]);length=np.linalg.norm(normal)
                if length<1e-8:continue
                normal/=length;ref=face['texture']
                for _ in range(15):
                    if not ref.startswith('#'):break
                    ref=model['textures'][ref[1:]]
                tex=np.array(self.texture(ref));u0,v0,u1,v1=face.get('uv',default_uv[side])
                uv=np.array([[u0,v0],[u1,v0],[u1,v1],[u0,v1]],dtype=float)/16
                uv=np.roll(uv,-face.get('rotation',0)//90,axis=0)
                faces.append((p,uv,tex,normal));points.extend(p)
        if not points:raise ValueError('Modèle sans volume : '+str(model)[:150])
        eye=np.array([1.25,1.1,1.65]);eye/=np.linalg.norm(eye)
        right=np.cross([0,1,0],eye);right/=np.linalg.norm(right);up=np.cross(eye,right)
        projection=np.stack([right,-up,eye],axis=1);projected=np.array(points)@projection
        lo=projected[:,:2].min(axis=0);hi=projected[:,:2].max(axis=0)
        scale=(size-18)/max(hi-lo);center=(lo+hi)/2
        rgba=np.zeros((size,size,4),dtype=np.uint8);depth=np.full((size,size),-np.inf)
        light=np.array([-.4,1,.5]);light/=np.linalg.norm(light)
        for p,uv,tex,n in faces:
            if np.dot(n,eye)<=0:continue
            q=p@projection;q[:,:2]=(q[:,:2]-center)*scale+size/2
            shade=.72+.28*max(0,float(np.dot(n,light)))
            for tri in [[0,1,2],[0,2,3]]:
                v=q[tri];t=uv[tri]
                low=np.maximum(0,np.floor(v[:,:2].min(axis=0)).astype(int))
                high=np.minimum(size-1,np.ceil(v[:,:2].max(axis=0)).astype(int))
                if np.any(high<low):continue
                yy,xx=np.mgrid[low[1]:high[1]+1,low[0]:high[0]+1];px=xx+.5;py=yy+.5
                a,b,c=v;den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
                if abs(den)<1e-9:continue
                wa=((b[1]-c[1])*(px-c[0])+(c[0]-b[0])*(py-c[1]))/den
                wb=((c[1]-a[1])*(px-c[0])+(a[0]-c[0])*(py-c[1]))/den;wc=1-wa-wb
                z=wa*a[2]+wb*b[2]+wc*c[2]
                u=wa*t[0,0]+wb*t[1,0]+wc*t[2,0];vv=wa*t[0,1]+wb*t[1,1]+wc*t[2,1]
                tx=np.clip(np.floor(u*tex.shape[1]).astype(int),0,tex.shape[1]-1)
                ty=np.clip(np.floor(vv*tex.shape[0]).astype(int),0,tex.shape[0]-1)
                color=tex[ty,tx].copy();color[:,:,:3]=(color[:,:,:3]*shade).astype(np.uint8)
                mask=(wa>=-1e-6)&(wb>=-1e-6)&(wc>=-1e-6)&(z>depth[yy,xx])&(color[:,:,3]>127)
                rgba[yy[mask],xx[mask]]=color[mask];depth[yy[mask],xx[mask]]=z[mask]
        return Image.fromarray(rgba)

def chest_model():
    # Coffre fermé : volumes du coffre, UV de entity/chest/normal (64×64).
    elements=[]
    for a,b,u,v in [([1,0,1],[15,10,15],0,19),([1,10,1],[15,15,15],0,0),([7,8,0],[9,12,1],0,0)]:
        w,h,d=np.array(b)-a
        uv={'up':[u+d,v,u+d+w,v+d],'down':[u+d+w,v,u+d+w+w,v+d],
            'west':[u,v+d,u+d,v+d+h],'north':[u+d,v+d,u+d+w,v+d+h],
            'east':[u+d+w,v+d,u+d+w+d,v+d+h],'south':[u+d+w+d,v+d,u+d+w+d+w,v+d+h]}
        elements.append({'from':a,'to':b,'faces':{s:{'texture':'#all','uv':[float(x)/4 for x in q]} for s,q in uv.items()}})
    return {'textures':{'all':'minecraft:entity/chest/normal'},'elements':elements}

def fit(im,size):
    out=Image.new('RGBA',(size,size));k=min(size/im.width,size/im.height)
    im=im.resize((max(1,round(im.width*k)),max(1,round(im.height*k))),Image.Resampling.NEAREST)
    out.alpha_composite(im,((size-im.width)//2,(size-im.height)//2));return out

def font(size,bold=False):
    name='DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    try:return ImageFont.truetype(name,size)
    except OSError:return ImageFont.load_default(size=size)

def recipe_image(assets,slots,result,count=1,smithing=False,shapeless=False):
    im=Image.new('RGBA',(560,300),'#c6c6c6');d=ImageDraw.Draw(im)
    d.rectangle((1,1,558,298),outline='#373737',width=3)
    d.line((4,295,4,4,555,4),fill='white',width=3)
    d.text((22,18),'TABLE DE FORGE' if smithing else 'TABLE DE CRAFT',font=font(20,True),fill='#343434')
    d.text((22,271),'Modèle de forge vide · base conservée' if smithing else ('Sans forme : ordre libre des ingrédients' if shapeless else 'Respecter les cases occupées et vides'),font=font(16),fill='#343434')
    def slot(x,y,item,quantity=None):
        d.rectangle((x,y,x+59,y+59),fill='#8b8b8b')
        d.line((x,y+59,x,y,x+59,y),fill='#373737',width=3)
        d.line((x+2,y+59,x+59,y+59,x+59,y+2),fill='white',width=3)
        if item:im.alpha_composite(fit(assets.icon(item),48),(x+6,y+6))
        if quantity is not None:
            text=str(quantity);w=d.textlength(text,font=font(20,True))
            d.text((x+56-w,y+39),text,font=font(20,True),fill='black',stroke_width=2,stroke_fill='black')
            d.text((x+55-w,y+38),text,font=font(20,True),fill='white')
    if smithing:
        for i,item in enumerate(slots):slot(24+i*76,115,item)
        for i,label in enumerate(['Vide','Base','Ajout']):d.text((28+i*76,190),label,font=font(15),fill='#343434')
    else:
        for i,item in enumerate(slots):slot(24+(i%3)*64,58+(i//3)*64,item)
    d.polygon([(281,136),(318,136),(318,122),(343,153),(318,182),(318,166),(281,166)],fill='#727272')
    slot(399,121,result,count)
    d.text((380,196),'Résultat',font=font(18,True),fill='#343434')
    if smithing:d.text((363,223),'objet amélioré',font=font(15),fill='#343434')
    return im.convert('RGB')
