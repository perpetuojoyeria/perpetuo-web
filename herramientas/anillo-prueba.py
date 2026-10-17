# Render de un anillo de PRUEBA más realista (banda plana pulida, reflejos de estudio).
# Solo para mostrar el efecto; se reemplaza por la foto real de un anillo Perpetuo.
import numpy as np, sys
from PIL import Image, ImageFilter
salida = sys.argv[1]; muestra = sys.argv[2]
N=1700; S=2; W=N*S
xs=np.linspace(-1.32,1.32,W); X,Y=np.meshgrid(xs,-xs)
R=1.0                      # radio del anillo
ancho, grosor = 0.085, 0.034   # media banda: ancho (a lo largo del eje) y grosor (radial); perfil abombado
tilt=np.radians(25); ct,st=np.cos(tilt),np.sin(tilt)
def local(px,py,pz):
    qy= ct*py - st*pz; qz= st*py + ct*pz
    return px,qy,qz
def sdf(px,py,pz):
    lx,ly,lz=local(px,py,pz)
    q=np.sqrt(lx**2+lz**2)-R
    # sección: óvalo achatado con bordes suaves (banda abombada, como un anillo de verdad)
    k=4.0  # superelipse: 2 = óvalo, más alto = más plano
    u=np.abs(q)/grosor; v=np.abs(ly)/ancho
    return ((u**k+v**k)**(1/k)-1)*min(grosor,ancho)*0.9
ox,oy=X,Y; oz=np.full_like(X,3.0); t=np.zeros_like(X); hit=np.zeros(X.shape,bool)
for i in range(260):
    d=sdf(ox,oy,oz-t); hit|=(d<5e-5); t=np.where(hit,t,t+d*0.6)
hit&=t<6
pz=oz-t; e=4e-4
nx=sdf(ox+e,oy,pz)-sdf(ox-e,oy,pz); ny=sdf(ox,oy+e,pz)-sdf(ox,oy-e,pz); nz=sdf(ox,oy,pz+e)-sdf(ox,oy,pz-e)
L=np.sqrt(nx**2+ny**2+nz**2)+1e-9; nx/=L; ny/=L; nz/=L
# dirección reflejada (vista = 0,0,-1)
rx,ry,rz=2*nz*nx,2*nz*ny,-1+2*nz*nz
# ——— Estudio de fotografía ———
hueso=np.array([251,251,244.])/255; noche=np.array([46,65,108.])/255; profundo=np.array([35,42,68.])/255; perla=np.array([255,253,203.])/255
el=np.arcsin(np.clip(ry,-1,1)); az=np.arctan2(rx,rz)
gris=noche*0.55+hueso*0.45
env=(profundo*0.7+gris*0.3)[None,None,:]+(gris-profundo*0.7-gris*0.3)[None,None,:]*np.clip(el*1.2+0.55,0,1)[...,None]
def caja(a0,a1,e0,e1,suav,int_,col):
    fa=np.clip(np.minimum(az-a0,a1-az)/suav,0,1); fe=np.clip(np.minimum(el-e0,e1-el)/suav,0,1)
    return (fa*fe)[...,None]*col*int_
env=env+caja(-2.6,-0.2,0.15,1.4,0.4,1.6,hueso)          # caja de luz grande arriba-izquierda (borde suave)
env=env+caja(0.7,1.4,-0.7,1.1,0.18,1.8,hueso)           # tira de luz vertical a la derecha
env=env+caja(-0.9,0.9,-1.2,-0.35,0.35,0.85,perla)           # rebote cálido abajo
env=env+caja(2.1,2.7,-0.3,0.6,0.15,1.1,hueso)            # tira trasera
env=env+caja(-3.3,-2.6,-0.4,0.4,0.2,0.8,hueso)
# metal plateado: reflectancia alta con Fresnel (Schlick) y tinte muy leve
F0=np.array([0.93,0.93,0.95]); cosv=np.abs(nz)[...,None]
F=F0+(1-F0)*(1-cosv)**5
col=env*F
# oclusión: la cara interna del aro recibe menos luz
lx,ly,lz=local(ox,oy,pz); radial=(nx*lx+ (ct*0)+ nz*0)  # aproximación
interior=(np.sqrt(lx**2+lz**2)<R-grosor*0.4)
col=np.where(interior[...,None], col*0.78, col)
# reflejo de punto (brillo intenso)
for dx_,dy_,dz_,p_,k_ in [(-0.5,0.7,0.5,220,2.0),(0.8,0.2,0.55,400,1.4)]:
    l=np.array([dx_,dy_,dz_]); l/=np.linalg.norm(l)
    col=col+(np.clip(rx*l[0]+ry*l[1]+rz*l[2],0,1)**p_*k_)[...,None]
# tono final (compresión suave de brillos)
col=1-np.exp(-col*1.25)
col=np.clip(col/ (1-np.exp(-1.25)) ,0,1)
img=np.zeros((W,W,4),np.uint8); img[...,:3]=(col*255).astype(np.uint8); img[...,3]=(hit*255).astype(np.uint8)
im=Image.fromarray(img,'RGBA').resize((N,N),Image.LANCZOS)
im=im.crop(im.getchannel('A').getbbox())
im.save(salida,optimize=True); print(im.size)
bg=Image.new('RGBA',im.size,(46,65,108,255)); bg.alpha_composite(im); bg.convert('RGB').save(muestra)
