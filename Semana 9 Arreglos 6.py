arreglo = {}
for x in range (0,10):
    arreglo[x] = int(input("Ingrese el valor:"))
    

for x in range(0,len(arreglo)):
    print("[",arreglo[x],"]",end=" ")

print("\n")
pos = int(input("Ingrese la posicion que desea modificar [0-9]: "))
valor = int(input("Ingrese el valor:"))
arreglo[pos] = valor

for x in range(0,len(arreglo)):
    print("[",arreglo[x],"]",end=" ")
