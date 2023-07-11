arreglo = {}
for x in range (0,10):
    valor=int(input("Ingrese el valor:"))
    arreglo[x] = valor

for x in range(0,len(arreglo)):
    print("[",arreglo[x],"]",end=" ")