// Configuración de Astro. Por ahora no hace falta nada especial:
// el sitio se genera como páginas estáticas, ideales para Cloudflare Pages.
import { defineConfig } from 'astro/config';

export default defineConfig({
  build: { inlineStylesheets: 'always' },
});
