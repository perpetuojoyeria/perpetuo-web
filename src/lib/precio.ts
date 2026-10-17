// Formato de precios en pesos colombianos: 89900 -> "$89.900"
export function formatoCOP(valor: number): string {
  const entero = Math.round(valor).toString();
  return '$' + entero.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
}
