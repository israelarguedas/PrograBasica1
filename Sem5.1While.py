#La pulperia Los Mas Caritos requiere un programa que
#permita sumar cada uno de los productos adquiridos
#por sus clintes y mostrar el total que deben pagar.
#Programe dicha solucion.

nombreProducto = ""
precioProducto = 0
precioTotal = 0
continuar = "s"

while continuar == "s":
    nombreProducto = input("Ingrese el nombre del producto: ")
    precioProducto = float(input("Ingrese el precio: "))
    precioTotal = precioProducto + precioTotal
    continuar = input("Desea ingresar otro producto (s/n)?")
print("El total a pagar es de:", precioTotal, "colones")