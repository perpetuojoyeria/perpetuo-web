// Revisa si un archivo existe en /public (fotos, videos, logos) al construir el sitio.
import fs from 'node:fs';
import path from 'node:path';

export function existeEnPublic(ruta?: string): boolean {
  if (!ruta) return false;
  return fs.existsSync(path.join(process.cwd(), 'public', ruta.replace(/^\//, '')));
}
