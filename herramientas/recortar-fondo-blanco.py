import numpy as np, sys
from PIL import Image
from scipy import ndimage as ndi
src, out, muestra = sys.argv[1:4]
# opcional: zona (x0 y0 x1 y1 en fracción de la foto) donde también se borra la sombra gris
zona = [float(v) for v in sys.argv[4:8]] if len(sys.argv) >= 8 else None
im = Image.open(src).convert('RGB')
a = np.asarray(im).astype(np.float32)
h, w, _ = a.shape
mn = a.min(2); mx = a.max(2)
blanco = (mn > 214) & (mx - mn < 16)                    # blanco o sombra gris clara, sin color
lab, n = ndi.label(blanco)
borde = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
# el hueco del anillo: la zona blanca más grande que no toca el borde
tam = ndi.sum(np.ones_like(lab), lab, index=np.arange(1, n + 1))
interiores = [i + 1 for i in np.argsort(-tam) if (i + 1) not in borde]
hueco = interiores[0]
print('zonas', n, 'hueco', hueco, int(tam[hueco - 1]))
fondo = np.isin(lab, list(borde) + [hueco])
if zona:
    yy, xx = np.mgrid[0:h, 0:w]
    dentro = (xx > zona[0] * w) & (yy > zona[1] * h) & (xx < zona[2] * w) & (yy < zona[3] * h)
    gris = (mn > 120) & (mx - mn < 22) & dentro
    lab2, _ = ndi.label(gris | fondo)
    fondo = np.isin(lab2, np.unique(lab2[fondo])) & (gris | fondo)
# borde suave: en una franja de 3 px alrededor del fondo, la transparencia sale de qué tan blanco es el pixel
franja = ndi.binary_dilation(fondo, iterations=3) & ~fondo
alfa = np.ones((h, w), np.float32)
alfa[fondo] = 0
lum = a.mean(2)
alfa[franja] = np.clip((255 - lum[franja]) / 60, 0, 1)
# quitar el halo blanco: des-mezclar el color contra el blanco
c = a.copy()
m = (alfa > 0) & (alfa < 1)
c[m] = (a[m] - (1 - alfa[m, None]) * 255) / alfa[m, None]
c = np.clip(c, 0, 255)
rgba = np.dstack([c, alfa * 255]).astype(np.uint8)
res = Image.fromarray(rgba, 'RGBA')
res = res.crop(res.getchannel('A').getbbox())
res.save(out, optimize=True); print(res.size)
bg = Image.new('RGBA', res.size, (46, 65, 108, 255)); bg.alpha_composite(res); bg.convert('RGB').save(muestra)
