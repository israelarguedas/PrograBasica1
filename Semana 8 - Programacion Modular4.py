#La tienda deportiva Play & Fun tiene sus articulos en promocion.
#El descuento se aplica segun el precio del producto. Escruba un
#programa qye npermita calcular e nuevo precio a cobrar al cliente
#Debe leer el precio y aplicar el descuento segun la siguiente tabla

#De 1000 a 3000 colones 5%
#De 3001 a 4000 colones 10%
#De 4001 a 5000 colones 15%
#Mas de 5000 colones 20%

#Muestre el nuevo precio. Debe enviar el precio a un metodo como
#parametro y calcular el nuevo precio. Muestre el nuevo precio en
#el cuerpo principal del programa

precio = 0
def calcularDescuento(precio):
    if(precio>=1000 and precio<=3000):
       precio = precio * 0.95
       print("El precio con el descuento aplicado es de:", precio, "\n")
    elif(precio>=3001 and precio<=4000):
        precio = precio * 0.90
        print("El precio con el descuento aplicado es de:", precio, "\n")
    elif(precio>=4001 and precio<=5000):
        precio = precio * 0.85
        print("El precio con el descuento aplicado es de:", precio, "\n")
    elif(precio > 5000):
        precio = precio * 0.80
        print("El precio con el descuento aplicado es de:", precio, "\n")
    else:
        precio = precio
        print("Este producto no posee descuento, el precio es de:", precio, "\n")

continuar = "s"

while (continuar == "s"):
    precio = float(input("\nBienvenidx al programa de calculo de descuentos\n"
    "Ingrese el precio del producto:"))
    calcularDescuento(precio)
    continuar = input("Desea ingresar un nuevo producto? (s/n):")

