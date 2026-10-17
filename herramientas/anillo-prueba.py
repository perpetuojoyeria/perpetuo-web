# Render de un anillo de PRUEBA: banda plateada abombada + circón talla brillante con 4 garras.
# Solo para mostrar el efecto del Hero; se reemplaza por la foto real de un anillo Perpetuo.
# Uso: python3 herramientas/anillo-prueba.py salida.png muestra.png
import numpy as np, sys
from PIL import Image
salida, muestra = sys.argv[1], sys.argv[2]
N, S = 1500, 2
W = N * S
xs = np.linspace(-1.32, 1.32, W)
X, Y = np.meshgrid(xs, -xs)
R = 1.0
ancho, grosor = 0.085, 0.034
tilt = np.radians(-26)                       # visto un poco desde arriba: el lado cercano queda abajo
ct, st = np.cos(tilt), np.sin(tilt)

def local(px, py, pz):
    return px, ct * py - st * pz, st * py + ct * pz

# ——— Circón ———
phi = np.radians(28)                          # posición sobre la banda (un poco a la derecha del frente)
u = np.array([np.sin(phi), 0.0, np.cos(phi)])  # eje de la piedra = hacia afuera de la banda
rg = 0.15                                     # radio del filetín
centro = u * (R + grosor + 0.075)
# base ortonormal alrededor del eje de la piedra
e1 = np.array([0.0, 1.0, 0.0]); e2 = np.cross(u, e1)
def planos(n, inclinacion, offset):
    lista = []
    for k in range(n):
        a = 2 * np.pi * k / n
        lat = np.cos(a) * e1 + np.sin(a) * e2
        nn = np.cos(inclinacion) * u + np.sin(inclinacion) * lat
        lista.append((nn, offset))
    return lista
# talla brillante: corona a 34°, facetas estrella cerca de la mesa, pabellón a 41°
corona = planos(16, np.radians(34), rg * np.sin(np.radians(34)))
r_e, h_e, a_e = rg * 0.62, rg * 0.22, np.radians(22)
estrella = planos(8, a_e, r_e * np.sin(a_e) + h_e * np.cos(a_e))
pabellon = [(-np.cos(np.radians(49)) * u + np.sin(np.radians(49)) * l, rg * np.sin(np.radians(49)) * 0.985)
            for l in [np.cos(2*np.pi*(k+0.5)/16) * e1 + np.sin(2*np.pi*(k+0.5)/16) * e2 for k in range(16)]]
mesa_h = rg * 0.30
def sdf_circon(lx, ly, lz):
    px, py, pz = lx - centro[0], ly - centro[1], lz - centro[2]
    h = px * u[0] + py * u[1] + pz * u[2]
    d = h - mesa_h                                               # mesa
    for nn, off in corona + estrella + pabellon:
        d = np.maximum(d, px * nn[0] + py * nn[1] + pz * nn[2] - off)
    rad = np.sqrt(np.maximum(px**2 + py**2 + pz**2 - h**2, 0))
    d = np.maximum(d, rad - rg)                                  # filetín
    return d

# garras: 4 cápsulas desde la banda hasta el borde de la piedra
garras = []
for k in range(4):
    a = np.pi / 4 + k * np.pi / 2
    lat = np.cos(a) * e1 + np.sin(a) * e2
    arriba = centro + lat * rg * 0.92 + u * 0.022
    abajo = u * (R + grosor * 0.6) + lat * rg * 0.5
    garras.append((abajo, arriba))
def sdf_capsula(lx, ly, lz, a, b, r):
    pa = np.stack([lx - a[0], ly - a[1], lz - a[2]]); ba = (b - a)[:, None]
    hh = np.clip((pa * ba).sum(0) / (ba * ba).sum(), 0, 1)
    q = pa - ba * hh
    return np.sqrt((q * q).sum(0)) - r

def sdf_todo(px, py, pz):
    lx, ly, lz = local(px, py, pz)
    q = np.sqrt(lx**2 + lz**2) - R
    k = 4.0
    banda = ((np.abs(q) / grosor)**k + (np.abs(ly) / ancho)**k)**(1 / k) - 1
    banda = banda * min(grosor, ancho) * 0.9
    piedra = sdf_circon(lx, ly, lz)
    garra = np.min([sdf_capsula(lx, ly, lz, a, b, 0.014) for a, b in garras], axis=0)
    metal = np.minimum(banda, garra)
    return np.minimum(metal, piedra), (piedra < metal)

# marcha de rayos solo sobre los rayos activos (más rápido)
ox, oy = X.ravel(), Y.ravel(); t = np.zeros_like(ox); hit = np.zeros(ox.shape, bool); vivo = np.ones(ox.shape, bool)
for i in range(320):
    idx = np.nonzero(vivo)[0]
    if idx.size == 0: break
    d, _ = sdf_todo(ox[idx], oy[idx], 3.0 - t[idx])
    t[idx] += d * 0.6
    h = d < 4e-5; hit[idx[h]] = True
    vivo[idx[h | (t[idx] > 6)]] = False
idx = np.nonzero(hit)[0]
px, py, pz = ox[idx], oy[idx], 3.0 - t[idx]
e = 3e-4
f = lambda a, b, c: sdf_todo(a, b, c)[0]
nx = f(px + e, py, pz) - f(px - e, py, pz); ny = f(px, py + e, pz) - f(px, py - e, pz); nz = f(px, py, pz + e) - f(px, py, pz - e)
L = np.sqrt(nx**2 + ny**2 + nz**2) + 1e-12; nx /= L; ny /= L; nz /= L
_, es_piedra = sdf_todo(px, py, pz)
rx, ry, rz = 2 * nz * nx, 2 * nz * ny, -1 + 2 * nz * nz

hueso = np.array([251, 251, 244.]) / 255; noche = np.array([46, 65, 108.]) / 255
profundo = np.array([35, 42, 68.]) / 255; perla = np.array([255, 253, 203.]) / 255
def estudio(rx, ry, rz):
    el = np.arcsin(np.clip(ry, -1, 1)); az = np.arctan2(rx, rz)
    gris = noche * 0.55 + hueso * 0.45
    env = (profundo * 0.7 + gris * 0.3)[None, :] + (gris - profundo * 0.7 - gris * 0.3)[None, :] * np.clip(el * 1.2 + 0.55, 0, 1)[:, None]
    def caja(a0, a1, e0, e1, s, k, col):
        fa = np.clip(np.minimum(az - a0, a1 - az) / s, 0, 1); fe = np.clip(np.minimum(el - e0, e1 - el) / s, 0, 1)
        return (fa * fe)[:, None] * col * k
    env = env + caja(-2.6, -0.2, 0.15, 1.4, 0.4, 1.6, hueso) + caja(0.7, 1.4, -0.7, 1.1, 0.18, 1.8, hueso)
    env = env + caja(-0.9, 0.9, -1.2, -0.35, 0.35, 0.85, perla) + caja(2.1, 2.7, -0.3, 0.6, 0.15, 1.1, hueso) + caja(-3.3, -2.6, -0.4, 0.4, 0.2, 0.8, hueso)
    return env

# metal
cosv = np.abs(nz)[:, None]
F0 = np.array([0.93, 0.93, 0.95]); F = F0 + (1 - F0) * (1 - cosv)**5
col = estudio(rx, ry, rz) * F
lx_, ly_, lz_ = local(px, py, pz)
interior = (np.sqrt(lx_**2 + lz_**2) < R - grosor * 0.4) & ~es_piedra
col[interior] *= 0.78
for l, p_, k_ in [((-0.5, 0.7, 0.5), 220, 2.0), ((0.8, 0.2, 0.55), 400, 1.4)]:
    l = np.array(l) / np.linalg.norm(l)
    col += (np.clip(rx * l[0] + ry * l[1] + rz * l[2], 0, 1)**p_ * k_)[:, None]

# circón: reflejo + "refracción" falsa + destellos por faceta
g = es_piedra
if g.any():
    refl = estudio(rx[g], ry[g], rz[g])
    # la luz entra por la corona, rebota en las facetas del pabellón y sale: patrón de caleidoscopio
    glx, gly, glz = local(px[g], py[g], pz[g])
    qx, qy, qz = glx - centro[0], gly - centro[1], glz - centro[2]
    a1 = qx * e1[0] + qy * e1[1] + qz * e1[2]; a2 = qx * e2[0] + qy * e2[1] + qz * e2[2]
    az = np.arctan2(a2, a1); rr = np.sqrt(a1**2 + a2**2) / rg
    sector = np.floor((az / (2 * np.pi) + 0.5) * 16)                 # 16 "flechas" simétricas, como un brillante
    anillo = np.floor(rr * 4)
    va = (sector + 0.5) * 2 * np.pi / 16
    vx = np.cos(va); vy = np.sin(va)
    ix = vx * 0.7 - rx[g] * 0.3; iy = vy * 0.7 - ry[g] * 0.3; iz = np.abs(rz[g]) * 0.6 + 0.4
    n_ = np.sqrt(ix**2 + iy**2 + iz**2); dentro = estudio(ix / n_, iy / n_, iz / n_)
    fres = (0.06 + 0.94 * (1 - np.abs(nz[g]))**5)[:, None]
    base = dentro * (1 - fres) * 1.2 + refl * fres
    fid = np.round(nx[g] * 9) * 131 + np.round(ny[g] * 9) * 17 + np.round(nz[g] * 9) * 7 + sector * 3.7 + anillo * 11.3
    rnd = (np.sin(fid * 12.9898) * 43758.5453) % 1.0
    claro = rnd > 0.5; oscuro = rnd < 0.22
    base[claro] = base[claro] * 0.35 + 1.3
    base[oscuro] = base[oscuro] * 0.25 + noche * 0.2
    tinte = np.where((rnd > 0.93)[:, None], perla[None, :] * 1.25, np.where(((rnd > 0.86) & (rnd <= 0.93))[:, None], np.array([0.82, 0.88, 1.0])[None, :] * 1.25, 1.0))
    col[g] = base * tinte

col = 1 - np.exp(-col * 1.25); col = np.clip(col / (1 - np.exp(-1.25)), 0, 1)
img = np.zeros((W * W, 4), np.uint8)
img[idx, :3] = (col * 255).astype(np.uint8); img[idx, 3] = 255
im = Image.fromarray(img.reshape(W, W, 4), 'RGBA').resize((N, N), Image.LANCZOS)
im = im.crop(im.getchannel('A').getbbox())
im.thumbnail((1400, 1400)); im.save(salida, optimize=True); print(im.size)
bg = Image.new('RGBA', im.size, (46, 65, 108, 255)); bg.alpha_composite(im); bg.convert('RGB').save(muestra)
