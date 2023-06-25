#Permita calcular el total a pagar por la compra de pantalones de vestir. Si se compran 
#entre 1 a 5 pantalones se aplica un descuento del 12.5%, si se compra una cantidad 
#comprendida entre 5 y 8 pantalones se aplica un descuento del 20% y si se compran 
#cantidades mayores, se aplica un descuento del 31.5% sobre el total de la compra. Debe 
#imprimirse en pantalla la compra final sin descuento, monto del descuento y la compra 
#con descuento. 

descuento1 = 0.875 #entre 1 a 5 pantalones se aplica un descuento del 12.5%
descuento2 = 0.80 #entre 5 y 8 pantalones se aplica un descuento del 20%
descuento3 = 0.685 #cantidades mayores, se aplica un descuento del 31.5% 

precioConDescuento = 0
cantidadPantalones = int(input("Ingrese la cantidad de pantalones a comprar:")) 
precioPantalones = float(input("Ingrese el precio de los pantalones:")) 

if (cantidadPantalones >= 1 and cantidadPantalones <= 5):
    precioPantalones = precioPantalones * cantidadPantalones
    precioConDescuento = precioPantalones * descuento1
    print ("El valor de la compra total sin descuento es de:", precioPantalones, 
           "\nEl monto del descuento es del 12.5%", 
           "\nEl valor de la compra total con descuento es de:", precioConDescuento)
elif (cantidadPantalones >= 5 and cantidadPantalones <= 8):
    precioPantalones = precioPantalones * cantidadPantalones
    precioConDescuento = precioPantalones * descuento2
    print ("El valor de la compra total sin descuento es de:", precioPantalones, 
           "\nEl monto del descuento es del 20%", 
           "\nEl valor de la compra total con descuento es de:", precioConDescuento)
elif (cantidadPantalones > 8):
    precioPantalones = precioPantalones * cantidadPantalones
    precioConDescuento = precioPantalones * descuento3
    print ("El valor de la compra total sin descuento es de:", precioPantalones, 
           "\nEl monto del descuento es del 31.5%", 
           "\nEl valor de la compra total con descuento es de:", precioConDescuento)
else:
    print("Ingrese un valor valido")

