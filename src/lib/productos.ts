// Funciones para leer los productos del JSON.
import datos from '../data/productos.json';
import metales from '../data/metales.json';

export type Metal = 'plata' | 'oro' | 'rodio';
export type Producto = (typeof datos.productos)[number] & { metales: Metal[] };

// solo las piezas disponibles ("disponible": false las oculta cuando se venden)
export const productos = (datos.productos as Producto[]).filter((p) => (p as { disponible?: boolean }).disponible !== false);
export const nombreMetal = (m: Metal) => metales[m].nombre;
export const precioDe = (p: Producto, m: Metal = p.metales[0]) => (p.precios as Record<string, number>)[m];
export const porCategoria = (cat: string) => productos.filter((p) => p.categoria === cat);
// las marcadas "Favorito"; si todavía no hay ninguna, las primeras del catálogo
export const favoritos = () => {
  const marcadas = productos.filter((p) => p.etiquetas.includes('Favorito'));
  return marcadas.length ? marcadas : productos;
};
