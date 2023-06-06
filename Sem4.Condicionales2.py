
montoXUnidad = float(input("Ingrese el monto del producto: "))
cantidadDeUnidades = int(input("Ingrese la cantidad de unidades: "))
Descuento = 0.20

precioTotal = montoXUnidad * cantidadDeUnidades


if (cantidadDeUnidades >= 12 ):
    precioDescuento = precioTotal * Descuento
    precioTotal = precioTotal - precioDescuento
    print("El precio total, incluyendo el descuento es:", precioTotal)
else:
    print("El precio total es:", precioTotal)