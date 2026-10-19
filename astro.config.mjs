// Configuración de Astro: sitio estático para Cloudflare Pages.
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://perpetuojoyeria.com',
  integrations: [
    // páginas privadas o de uso interno no van al mapa del sitio
    sitemap({ filter: (pagina) => !['/componentes', '/bolsa', '/cuenta', '/buscar', '/404'].some((r) => pagina.includes(r)) }),
  ],
  // direcciones sin barra al final (/aretes), como las sirve Cloudflare Pages
  trailingSlash: 'never',
  build: { inlineStylesheets: 'always', format: 'file' },
});
