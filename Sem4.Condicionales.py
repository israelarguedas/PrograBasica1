#Condicionales

edadCliente = int(input("Ingrese la edad del cliente: "))

if (edadCliente < 3 or edadCliente > 65):
    print("Su entrada es gratis")
else:
    print("El monto de su entrada es de 1500 colones")