// Punto único para "cerrar" un pedido.
// Hoy (v1) el pedido se envía por WhatsApp con el mensaje ya escrito.
// Mañana, para cobrar en línea, se agrega otro "proveedor" (Wompi, Bold, ePayco…) en esta carpeta
// y se cambia PROVEEDOR: la página /bolsa no necesita cambiar.
import type { ItemBolsa } from '../bolsa';
import { whatsapp } from './whatsapp';

export type DatosPedido = {
  nombre: string;
  ciudad: string;
  metodo: string;        // cómo quiere pagar: PSE, tarjeta, contraentrega…
  nota?: string;
};

export type Pedido = {
  items: ItemBolsa[];
  subtotal: number;
  envioGratis: boolean;
  datos: DatosPedido;
};

// Lo que devuelve un proveedor: a dónde mandar a la clienta para terminar
export type ResultadoPago = { tipo: 'redireccion'; url: string };

export interface ProveedorPago {
  nombre: string;
  iniciar(pedido: Pedido): Promise<ResultadoPago> | ResultadoPago;
}

const PROVEEDOR: ProveedorPago = whatsapp;

export const iniciarPago = (pedido: Pedido) => PROVEEDOR.iniciar(pedido);
