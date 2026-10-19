PORCENTAJE_IVA = 13
IMPUESTO_TRANSACCIONES = 3
def CalcularPrecio(precio,porcentajeDescuento):
    montoDescuento = precio * (porcentajeDescuento / 100)
    precioSubTotal = precio - montoDescuento
    montoFacturado = precioSubTotal * ((PORCENTAJE_IVA / 100)+(IMPUESTO_TRANSACCIONES / 100))
    precioFinal = precioSubTotal + montoFacturado
    return precioFinal
def ValidarPrecio(precio):
    # Validar que el precio sea mayor a cero, si no lo es, retornar un mensaje de error, de lo contrario retornar True, variable tenga strip
   

def EjecutarModuloCaja():
    print("Bienvenido al módulo de caja")
    sistemaActivo=True
    while sistemaActivo:
        print("Ingrese el precio del producto: ")
        precio = input()
        if ValidarPrecio(precio):
            print("Ingrese el porcentaje de descuento: ")
            porcentajeDescuento = int(input())
            precioFinal = CalcularPrecio(float(precio), float(porcentajeDescuento))
            print(f"El precio final del producto es: {precioFinal}")
        else:
            print("Error: El precio debe ser mayor a cero.")
        print("¿Desea calcular otro producto? (s/n): ")
        respuesta = input().strip().lower()
        if respuesta != 's':
            sistemaActivo = False

EjecutarModuloCaja()

