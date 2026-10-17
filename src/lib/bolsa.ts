// La bolsa de compras vive en el navegador de cada clienta (localStorage).
// No necesita servidor: si borra los datos del navegador, la bolsa se vacía.
// Cada vez que cambia, avisa con el evento "bolsa:cambio" para que el encabezado y la página /bolsa se actualicen.

export type ItemBolsa = {
  id: string;            // slug + metal + modo: la misma pieza en otro metal es otra línea
  slug: string;
  nombre: string;
  metal: string;
  precio: number;
  cantidad: number;
  tipo?: 'producto' | 'mystery-box';
  modo?: string;         // solo Mystery Box: "Una vez" o "Cada mes"
};

const CLAVE = 'perpetuo-bolsa';
const MAXIMO = 10;       // tope por línea, para evitar toques de más

export function leer(): ItemBolsa[] {
  try {
    const datos = JSON.parse(localStorage.getItem(CLAVE) || '[]');
    return Array.isArray(datos) ? datos.filter((i) => i && i.id && i.precio > 0 && i.cantidad > 0) : [];
  } catch {
    return [];
  }
}

// Si el navegador no deja guardar (modo privado), la bolsa dura solo esta visita
let sePuedeGuardar = true;
let memoria: ItemBolsa[] = [];
const actual = () => (sePuedeGuardar ? leer() : memoria.map((i) => ({ ...i })));

function guardar(items: ItemBolsa[]) {
  try { localStorage.setItem(CLAVE, JSON.stringify(items)); } catch { sePuedeGuardar = false; }
  memoria = items;
  window.dispatchEvent(new CustomEvent('bolsa:cambio', { detail: { items } }));
}

export function agregar(item: Omit<ItemBolsa, 'id' | 'cantidad'>, cantidad = 1) {
  const id = [item.slug, item.metal, item.modo].filter(Boolean).join('|');
  const items = actual();
  const existente = items.find((i) => i.id === id);
  if (existente) existente.cantidad = Math.min(MAXIMO, existente.cantidad + cantidad);
  else items.push({ ...item, id, cantidad });
  guardar(items);
}

export function cambiarCantidad(id: string, cantidad: number) {
  const items = actual()
    .map((i) => (i.id === id ? { ...i, cantidad: Math.min(MAXIMO, cantidad) } : i))
    .filter((i) => i.cantidad > 0);
  guardar(items);
}

export const quitar = (id: string) => cambiarCantidad(id, 0);
export const vaciar = () => guardar([]);
export const lista = () => actual();
export const cuenta = (items = actual()) => items.reduce((n, i) => n + i.cantidad, 0);
export const subtotal = (items = actual()) => items.reduce((n, i) => n + i.precio * i.cantidad, 0);
export const formatoCOP = (n: number) => '$' + Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.');
