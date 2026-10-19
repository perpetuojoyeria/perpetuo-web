# Cómo publicar Perpetuo en perpetuojoyeria.com

Esta guía es para hacerla una sola vez. Después, cada cambio que guardes en GitHub se publica solo en 1 o 2 minutos.

---

## Antes de lanzar: lo que falta llenar

Busca estos marcadores entre [CORCHETES] y cámbialos por los datos reales. Todos están en la carpeta `src/data`, y puedes editarlos directamente en GitHub: abre el archivo, toca el lápiz ✏️, cambia el texto y toca **Commit changes**.

| Archivo | Qué llenar |
|---|---|
| `sitio.json` | Usuario de Instagram (por ejemplo `@perpetuojoyeria`) |
| `politicas.json` | Tiempo de despacho y de entrega, cobertura de envíos, días para cambios, condición de cambio de aretes, tiempo de garantía |
| `confianza.json` y `anuncios.json` | Tiempo de garantía, días de cambio, cobertura de envíos |
| `bolsa.json` | Costo de envío, ciudades con contraentrega |
| `mystery-box.json` | Mes, día de corte, día de cobro, días de llegada, condiciones de garantía, cómo evitan piezas repetidas, **precios y valores reales** (hoy son de ejemplo) y `"placeholder": false` |
| `paginas.json` | Tu historia (Nosotras), horario, correo, tiempo de respuesta, quién paga el envío de un cambio, cuidados de cada metal (micras, duración del baño) |
| `productos.json` | Los productos reales (hoy hay 12 de ejemplo con `"placeholder": true`) |

**Fotos** (si falta una, el sitio muestra un espacio gris con la nota de qué foto va ahí):
- `public/fotos/productos/` → fotos de cada producto (el nombre exacto está en `productos.json`)
- `public/fotos/mystery-box/` → `caja-plata.jpg`, `caja-oro.jpg`, `caja-rodio.jpg`
- `public/fotos/looks/` → una foto por look (los nombres están en `looks.json`)
- `public/fotos/nosotras/fundadora.jpg`
- `public/fotos/hero/anillo.png` → el anillo real sin fondo. Mientras no esté, se usa el de prueba.
- Ideal: un video del Hero con joyas reales de Perpetuo (`public/videos/hero.mp4`).

---

## Paso 1. Crear la cuenta en Cloudflare

1. Entra a **dash.cloudflare.com** y crea una cuenta gratis con el correo de la marca.
2. Confirma el correo.

## Paso 2. Conectar el sitio con GitHub

1. En el menú de la izquierda entra a **Workers & Pages** (en algunas cuentas aparece como **Compute → Workers & Pages**).
2. Toca **Create** (Crear) → pestaña **Pages** → **Connect to Git** (Conectar con Git).
3. Elige **GitHub** y autoriza a Cloudflare. Cuando pregunte a qué repositorios, elige **perpetuojoyeria/perpetuo-web**.
4. Selecciona el repositorio **perpetuo-web** y toca **Begin setup**.

## Paso 3. Configuración de la publicación

Llena así (copia y pega):

| Campo | Valor |
|---|---|
| Project name | `perpetuo` |
| Production branch | `main` |
| Framework preset | `Astro` |
| Build command | `npm run build` |
| Build output directory | `dist` |

Abre **Environment variables** y agrega una:
- Variable name: `NODE_VERSION` · Value: `22`

Toca **Save and Deploy**. En 1 o 2 minutos aparece una dirección como `perpetuo.pages.dev`. Ábrela en el celular para revisar que todo esté bien.

## Paso 4. Conectar el dominio perpetuojoyeria.com

1. Dentro del proyecto `perpetuo`, entra a **Custom domains** → **Set up a custom domain**.
2. Escribe `perpetuojoyeria.com` y sigue los pasos. Luego repite con `www.perpetuojoyeria.com`.
3. Lo que pase después depende de dónde compraste el dominio:
   - **Si lo compraste en Cloudflare:** se conecta solo.
   - **Si lo compraste en otro lado** (GoDaddy, Namecheap, Hostinger…): lo más fácil es pasar el dominio a Cloudflare. Cloudflare te dará dos "nameservers" (algo como `ana.ns.cloudflare.com`). Entra a la página donde compraste el dominio, busca **Nameservers / Servidores DNS**, reemplaza los que hay por esos dos y guarda. Puede tardar desde unos minutos hasta 24 horas.
4. Cuando el dominio diga **Active**, el sitio ya está en `https://perpetuojoyeria.com`, con candado de seguridad incluido.

## Paso 5. Avisarle a Google

1. Entra a **search.google.com/search-console** con el correo de la marca.
2. Toca **Agregar propiedad** → **Dominio** → escribe `perpetuojoyeria.com`.
3. Google te pide verificarlo con un registro "TXT". Si el dominio está en Cloudflare, Google ofrece hacerlo automáticamente: acepta.
4. Ya verificado, entra a **Sitemaps**, escribe `sitemap-index.xml` y toca **Enviar**.

Google tarda unos días en empezar a mostrar el sitio.

---

## Cómo hacer cambios después

- **Textos, precios o productos:** edita el archivo `.json` en GitHub (lápiz ✏️ → **Commit changes**). En 1 o 2 minutos se ve en la página.
- **Fotos:** en GitHub entra a la carpeta (por ejemplo `public/fotos/productos`), toca **Add file → Upload files**, sube la foto con el nombre exacto y toca **Commit changes**.
- **Si algo sale mal:** en Cloudflare, en **Deployments**, puedes volver a cualquier versión anterior con **Rollback**.

## Cuando quieras cobrar en línea

Hoy los pedidos llegan por WhatsApp. Para cobrar dentro de la página (Wompi, Bold, ePayco…), el código de pago está separado en `src/lib/checkout`. Hay que crear la cuenta en la pasarela y agregar un "proveedor" nuevo en esa carpeta; el resto del sitio no cambia. Las pasarelas piden una pequeña función en el servidor, y Cloudflare Pages la permite (Pages Functions) sin cambiar de hosting.
