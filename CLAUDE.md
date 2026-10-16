# Perpetuo Joyería — Brief del proyecto

La usuaria no es programadora: explicar todo en lenguaje simple, en español, tuteando.

## LA MARCA
Perpetuo es una marca de joyería en Medellín (Colombia). Vende piezas en tres materiales que forman una escalera de valor: rodio (entrada), plata 925 (el corazón de la colección) y oro laminado (el capricho). Tiene una mystery box mensual en tres versiones: plata, oro laminado y rodio.
- Tagline: "Brillo que se queda."
- Personalidad: juvenil, fresca, coqueta, ingeniosa, segura. NO es la joyería tradicional con vitrina y vendedor serio, ni el bazar de bisutería.
- Público: mujeres jóvenes que se arman el look por capas, regalan con intención y usan joyas a diario. La mayoría compra desde el celular.

## REFERENCIAS
- Studs (studs.com): energía joven, tono de amiga, vender combinaciones de piezas ("looks") en vez de piezas sueltas para que den ganas de seguir explorando.
- Monica Rich Kosann (monicarichkosann.com): acabado editorial, color en bloques detrás del producto, sección "cómo usarlo" con piezas apiladas, y la idea de que cada joya cuenta la historia de quien la lleva.
- Objetivo central: en los primeros segundos la usuaria debe sentir la necesidad de seguir explorando.

## PALETA (solo estos 4 colores)
- Blanco Hueso #FBFBF4: fondo general.
- Azul Noche #2E416C: texto principal, botones, bloques de marca.
- Azul Profundo #232A44: bloques oscuros, footer.
- Amarillo Perla #FFFDCB: acento para lo especial (mystery box, etiquetas, anuncios). Con moderación, para que siempre signifique "aquí pasa algo".

## TIPOGRAFÍA (Google Fonts)
- Italiana: títulos de sección en mayúsculas espaciadas.
- Cormorant Garamond itálica: frases coquetas y nombres de colección.
- Jost: textos, precios, menú y botones.
- Caveat: notas de precio escritas a mano (solo números o frases de 1 a 3 palabras).
- Máximo tres familias por sección.

## SELLOS VISUALES
- Marco circular: las fotos principales de categoría van recortadas en círculo con borde fino.
- La estrella de cuatro puntas del logo es el único ícono decorativo. Nada de corazones, brillos genéricos ni emojis.
- Botones tipo píldora. Tarjetas de producto con esquinas redondeadas de 24px.
- Los logos van en la carpeta public/logos (el encabezado busca perpetuo-horizontal.svg/.png). Nunca redibujar ni reescribir el logotipo con una fuente: usar siempre el archivo.

## FOTOGRAFÍA
Luz natural, fondos lisos en la paleta, la mitad de las fotos con la joya puesta (oreja, cuello, mano). Mientras no haya fotos reales, usar marcadores de posición con una etiqueta que describa la foto que va ahí.

## VOZ
- Tuteamos siempre, como una amiga. Frases cortas.
- Material y precio siempre claros. Un guiño ingenioso por sección, no cinco.
- Palabras sí: brillo, destello, capas, ritual, para siempre, edición del mes.
- Palabras no: "bisutería fina", "réplica", "económico", "inversión", "exclusivo".
- No inventar precios, productos ni cifras: usar marcadores como [PRECIO] o [NOMBRE DE LA PIEZA].

## STACK TÉCNICO
- Sitio propio publicado en Cloudflare Pages con dominio propio.
- Framework: Astro. Cada sección es un componente independiente en /src/components que se ensambla en la página de inicio.
- Colores, tipografías, radios y espaciados como variables CSS globales en un solo archivo (src/styles/global.css).
- Productos, looks y la mystery box del mes en archivos JSON separados del diseño (src/data/), para que el equipo pueda cambiar piezas sin tocar el código.
- Mobile first, rápido y liviano: imágenes optimizadas, sin librerías innecesarias.
- El sistema de pago aún no está definido (WhatsApp, pasarela colombiana o mixto). NO construir carrito ni pagos hasta que se indique.

## HOJA DE RUTA DEL HOME
1. Barra de anuncio + encabezado
2. Hero
3. Looks Perpetuo (combinaciones con puntos tocables sobre cada pieza)
4. Compra por material
5. El secreto del mes (mystery box)
6. Las favoritas (más vendidos)
7. Cómo usarlo
8. Tu historia con Perpetuo (fotos de clientas)
9. Footer

## REGLAS DE TRABAJO
- Construir UNA sección a la vez. No avanzar a la siguiente hasta que la usuaria la apruebe.
- Al terminar cada sección, explicar en 2 o 3 líneas qué decisiones de diseño se tomaron y por qué, y cómo verla en el navegador.
- Si algo no está claro, preguntar antes de suponer.

## ESTADO
- [x] Paso 1: Barra de anuncio + encabezado (aprobado). Logo: monograma sin fondo en public/logos/perpetuo-monograma.png; falta versión horizontal y versión clara para el footer.
- [ ] Paso 2: Hero con video (en revisión). Video en public/videos (ver LEEME.txt), textos en src/data/hero.json. Notita Caveat de precio reservada para Looks (regla de 3 familias).
