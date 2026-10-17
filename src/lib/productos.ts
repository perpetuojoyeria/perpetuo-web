// Funciones para leer los productos del JSON.
import datos from '../data/productos.json';
import metales from '../data/metales.json';

export type Metal = 'plata' | 'oro' | 'rodio';
export type Producto = (typeof datos.productos)[number] & { metales: Metal[] };

export const productos = datos.productos as Producto[];
export const nombreMetal = (m: Metal) => metales[m].nombre;
export const precioDe = (p: Producto, m: Metal = p.metales[0]) => (p.precios as Record<string, number>)[m];
export const porCategoria = (cat: string) => productos.filter((p) => p.categoria === cat);
export const favoritos = () => productos.filter((p) => p.etiquetas.includes('Favorito'));
