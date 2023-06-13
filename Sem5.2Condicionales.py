#Los patos de un grajero se venden acon un descuento de 5000 
#si su valor es mayor a los 20000, en caso contrario solo se 
#hara un rebajo de 2000 colones. Escriba un programa que lea 
#el precio del pato, aplique el descuento y determine el nuevo precio. 
#Asuma que los patos valen al menos 3000 colones
  
precioPato = 0
descuento1 = 2000
descuento2 = 5000
nuevoPrecio = 0

precioPato = float(input("Ingrese el precio del pato (El precio del pato no puede ser menor a 3000 colones): "))

while (precioPato < 3000): # Bucle para limitar el valor de diasSemana
    print("El precio ingresado es invalido, ingrese un valor mayor o igual a 3000")
    precioPato = float(input("Ingrese el precio del pato (El precio del pato no puede ser menor a 3000 colones): "))
else:
    if (precioPato > 20000 ):
        nuevoPrecio = precioPato - descuento2
        print("El valor del pato es de:", nuevoPrecio)
    else:
        nuevoPrecio = precioPato - descuento1
        print("El valor del pato es de:", nuevoPrecio)
