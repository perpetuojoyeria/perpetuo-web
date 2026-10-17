// Proveedor v1: arma el mensaje del pedido y abre WhatsApp con el número de la tienda.
import sitio from '../../data/sitio.json';
import metales from '../../data/metales.json';
import { formatoCOP } from '../bolsa';
import type { Pedido, ProveedorPago } from './index';

const nombreMetal = (m: string) => (metales as Record<string, { nombre: string }>)[m]?.nombre ?? m;

export function mensajePedido({ items, subtotal, envioGratis, datos }: Pedido) {
  const lineas = items.map((i) => {
    const modo = i.modo ? ` · ${i.modo}` : '';
    return `• ${i.cantidad} × ${i.nombre} (${nombreMetal(i.metal)}${modo}) — ${formatoCOP(i.precio * i.cantidad)}`;
  });
  return [
    `¡Hola, Perpetuo! Quiero hacer este pedido:`,
    '',
    ...lineas,
    '',
    `Subtotal: ${formatoCOP(subtotal)}`,
    envioGratis ? 'Envío: gratis' : 'Envío: por confirmar según mi ciudad',
    '',
    `Nombre: ${datos.nombre}`,
    `Ciudad: ${datos.ciudad}`,
    `Quiero pagar con: ${datos.metodo}`,
    datos.nota ? `Nota: ${datos.nota}` : '',
  ].filter((l, i, arr) => !(l === '' && arr[i - 1] === '')).join('\n').trim();
}

export const whatsapp: ProveedorPago = {
  nombre: 'WhatsApp',
  iniciar(pedido) {
    return { tipo: 'redireccion', url: `https://wa.me/${sitio.whatsapp}?text=${encodeURIComponent(mensajePedido(pedido))}` };
  },
};
