// Configuración de Astro: sitio estático para Cloudflare Pages.
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://perpetuojoyeria.com',
  integrations: [
    sitemap({ filter: (pagina) => !pagina.includes('/componentes') }),
  ],
  build: { inlineStylesheets: 'always' },
});
