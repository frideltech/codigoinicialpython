PORCENTAJE_IVA = 13
IMPUESTO_TRANSACCIONES = 3
def calcularPrecio(precio,porcentajeIva, porcentajeIT,porcentajeDescuento):
    montoDescuento = precio * (porcentajeDescuento / 100)
    precioSubTotal = precio - montoDescuento
    montoIva = precioSubTotal * (PORCENTAJE_IVA / 100)
    return montodescuento


