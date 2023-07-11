#En una sala de teatro se requiere almacenar los nombres de las personas
#que ocuparán las butacas de una fila, cada fila tiene 10 butacas. Cree
#un programa que almacena los nombres en las posiciones que le van
#indicando, por ejemplo: Ana Jiménez, 4 (el cuatro indica el número de
#butaca).

x = 0
arreglo = ["","","","","","","","","",""]
counter = 1

while counter <= 10:
    x = int(input("Ingrese la posicion que desea modificar [0-9]: "))
    nombre = input("Ingrese el nombre:")
    if x<=9 and arreglo[x] == "":
        arreglo[x] = nombre
        print("El asiento ", x, "fue ocupado por:", arreglo[x])
        print("Hay", counter, "asientos ocupados")
        counter = counter+1

for x in range(0,len(arreglo)):
    print("[Numero de asiento:", x, "Espectador", arreglo[x],"]",end=" ")