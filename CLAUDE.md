# Perpetuo Joyería — Brief del proyecto

La usuaria no es programadora: explicar todo en lenguaje simple, en español, tuteando.
Este brief (versión 2) reemplaza al anterior. Decisiones confirmadas por la usuaria están marcadas ✔.

## LA MARCA
Perpetuo es una marca colombiana de joyería (Medellín) en tres materiales que forman una escalera de valor: rodio (entrada), plata 925 (el corazón) y oro laminado (el capricho). Tiene una Mystery Box mensual en tres versiones: plata, oro laminado y rodio.
- Tagline: "Brillo que se queda."
- Vibra: juvenil, fresca y coqueta, distinta a las joyerías genéricas. Humor y personalidad, pero no infantil.
- Idioma: español colombiano, cercano y casual. Tuteamos.
- Público: mujeres jóvenes que se arman el look por capas, regalan con intención y usan joyas a diario. Llegan sobre todo desde Instagram y WhatsApp, en el celular.

## DATOS DEL SITIO (src/data/sitio.json)
- WhatsApp de pedidos ✔: 305 338 7593 (enlace: 573053387593)
- Envío gratis desde ✔: $250.000
- Dominio ✔: perpetuojoyeria.com
- Publicación: Cloudflare Pages. NO usar Shopify.

## PALETA (solo estos 4 colores, no agregar otros)
- Azul Noche #2E416C: texto principal y bloques fuertes.
- Azul Profundo #232A44: fondos oscuros, footer, sellos.
- Amarillo Perla #FFFDCB: botones, sellos de precio, etiquetas y ✔ (cambio v3) bandas y bloques puntuales de fondo (franja que se mueve, bloque Mystery Box, algunos bloques de categoría). NUNCA como fondo general de la página.
- Blanco Hueso #FBFBF4: fondo principal.
- Se permiten transparencias de estos mismos colores (líneas, sombras, velos).
- Amarillo Perla y Blanco Hueso casi no contrastan: un botón amarillo sobre fondo claro lleva borde Azul Noche. Texto sobre amarillo siempre en Azul Noche.
- Punticos de metal (sin agregar colores): oro laminado = Amarillo Perla con borde; plata = Blanco Hueso con borde; rodio = Azul Noche suave (gris azulado). Siempre con nombre accesible.
- El logo tiene un tono violeta propio: no se toca, pero el diseño solo usa los 4 colores.

## TIPOGRAFÍA ✔ (cambio v3: estilo Studs)
- Archivo (variable, ancho y extra gruesa, 800-900): títulos. ✔ Títulos cortos (1 a 4 palabras) en MAYÚSCULAS gruesas. Fraunces quedó descartada ("se veía hecha por IA").
- Jost: textos, precios, menú, nombres de producto y botones (botones en 600). En minúscula normal.
- Solo estas dos familias en todo el sitio.
- Textos largos, precios y nombres de producto nunca en mayúsculas. No cambiar una sola palabra del título a cursiva/serif como "decoración".

## SELLOS VISUALES
- La estrella de cuatro puntas del logo es el único ícono decorativo (archivo: public/logos/perpetuo-estrella.png, recortado del original). Nada de corazones, brillos genéricos ni emojis.
- Botones tipo píldora, color sólido, letra gruesa. ✔ (v3) Fotos, tarjetas y bloques con ESQUINAS RECTAS, de borde a borde y casi sin espacio entre ellas (estilo Studs).
- Usar la estrella con moderación (franja que se mueve, sellos). Evitar el "look de plantilla IA": nada de tarjetas redondeadas con sombra suave, cajas punteadas, degradados ni exceso de aire.
- Chips de subcategoría con foto en círculo y borde fino.
- Logo: public/logos/perpetuo-monograma.png (monograma recortado sin fondo). Originales en public/logos/originales. Falta versión horizontal y versión clara para fondos oscuros. Nunca redibujar ni reescribir el logotipo.

## REFERENCIAS (sacar ideas, NO copiar)
- Studs (principal, energía): botones sólidos con letra gruesa, home con cuadrícula de bloques de distintos tamaños por categoría y "moods", fotos con personalidad, "Mystery Sets" con nombre de juego de palabras, sello de precio, valor tachado y selector de metal.
- Mejuri (catálogo y ficha): chips con foto para subcategorías, punticos de metal en cada tarjeta, etiquetas tipo "Favorito", franja de confianza, bloque "Por qué lo amamos" con datos concretos.
- Pura Vida Bracelet Club (suscripción): tarjetas de plan, fechas de cobro y envío explícitas, "cancela cuando quieras", FAQ con humor.
- Evitar: nombres técnicos en mayúscula ("CADENA 5MM 60CM 6543"), fondo crema con dorados genéricos, plantilla banner → grilla → newsletter sin personalidad, morados/índigos por defecto.

## FOTOGRAFÍA
- Hero: anillo que atraviesa el título (mitad detrás y mitad delante de las letras, flota suave). Hoy usa public/fotos/hero/anillo-prueba.png (aro liso de PRUEBA, generado solo para mostrar el efecto; no es un producto). Reemplazar por public/fotos/hero/anillo.png: foto real PNG sin fondo, anillo visto un poco desde arriba (óvalo), mínimo 1600 px.
Fotos con personalidad, luz natural, fondos lisos en la paleta, la mitad con la joya puesta. Si falta una foto: espacio con la proporción correcta y nota de dirección de arte. NUNCA dibujar joyas falsas con CSS.

## VOZ
- Frases cortas, tono de amiga. Un guiño ingenioso por sección, no cinco.
- Material y precio siempre claros. Precio en COP con formato $89.900.
- Nombres de producto cortos y bonitos.
- Palabras sí: brillo, destello, capas, ritual, para siempre, edición del mes.
- Palabras no: "bisutería fina", "réplica", "económico", "inversión", "exclusivo".
- No inventar datos reales (precios, micras, políticas). Los 12 productos de ejemplo van marcados como placeholder; políticas con marcadores [ASÍ].

## STACK TÉCNICO ✔
- Astro estático, sin backend. JS mínimo y sin librerías (solo @astrojs/sitemap e imágenes optimizadas).
- Tokens de diseño en UN archivo: src/styles/tokens.css. Estilos generales en src/styles/base.css.
- Datos en src/data/*.json (productos, categorías, looks, mystery box, confianza, sitio).
- Componentes: src/components/base (ladrillos), layout (anuncio, encabezado, footer), secciones.
- Bolsa en el navegador (localStorage). Pago v1: pedido prellenado por WhatsApp. Código de pago separado en src/lib/checkout para conectar una pasarela después (Wompi, Bold, ePayco…).
- Calidad: mobile first (revisar en 375 px y escritorio), contraste AA, foco visible, alt, teclado, lazy loading, SEO básico (title, description, Open Graph, sitemap).

## PÁGINAS
1. Home: Hero con VIDEO ✔ y CTA amarillo · cuadrícula de bloques de categorías y moods · Looks Perpetuo ✔ (combinaciones con puntos tocables sobre cada pieza) · Mystery Box del mes · Favoritos · franja de confianza.
2. Catálogo por categoría (aretes, collares, anillos, pulseras, sets): chips con foto, filtro por metal, tarjetas con foto, nombre, precio, punticos, etiqueta opcional, botón "Agregar +".
3. Ficha de producto: galería, selector de metal, precio, "Agregar a la bolsa", franja de confianza, "Por qué lo amamos" (material, micras, hipoalergénico, cuidados), acordeones (envío, cambios, garantía), "Combínalo con".
4. Mystery Box: 3 tarjetas (plata, oro laminado, rodio) con nombre con gracia, sello de precio, "valor garantizado de $X", número de piezas, una vez o mensual · "Cómo funciona" en 3 pasos · fechas de cobro y llegada · FAQ (incluye "¿me puedo salir cuando quiera?") · qué no tiene cambio.
5. Bolsa y pago: barra de progreso hacia envío gratis ($250.000), resumen, métodos visibles (PSE, tarjeta, contraentrega, Addi/Sistecrédito, WhatsApp), pedido por WhatsApp con mensaje prellenado.
6. Mi cuenta / suscripción (maqueta con datos de ejemplo): próximo cobro y envío, metal elegido y cambiarlo, pausar / saltar un mes / cancelar, historial de cajas.
7. Nosotras, Cuidados de la joya, Envíos y cambios, Contacto.
- Menú: Aretes · Collares · Anillos · Pulseras · Sets · Looks · Mystery Box.

## ETAPAS (mostrar cada una y esperar aprobación)
1. Tokens y componentes base (+ adaptar encabezado y Hero a las reglas nuevas)
2. Home
3. Catálogo y Ficha
4. Mystery Box
5. Bolsa
6. Cuenta + páginas informativas + SEO + pasos para publicar en Cloudflare Pages

## REGLAS DE TRABAJO
- Una etapa a la vez; no avanzar sin aprobación.
- Al terminar cada etapa: 2-3 líneas de decisiones de diseño y por qué, y cómo verla.
- Si algo no está claro, preguntar antes de suponer.

## ESTADO
- [x] Etapa 1: tokens y componentes base (aprobada). Muestrario interno en /componentes (no sale en Google). Dominio confirmado: perpetuojoyeria.com.
- [ ] Etapa 2: Home. Primera versión RECHAZADA ("se ve hecha por Claude"). Rediseño v3 estilo Studs en revisión. Datos: home.json, looks.json, mystery-box.json (valores de ejemplo).
