#Se requiere un programa que imprima una palabra al revés. Debe funcionar para
#cualquier palabra, por lo cual debe utilizar ciclos.

palabra={}
palabra02=""
palabra02=input("Digite una palabra:")
for x in range(0,len(palabra02)):
    palabra[x]=palabra02[x]
for x in range(0,len(palabra)):
    print(palabra[x],end="")
print("\n\n")
for x in range(len(palabra)-1,-1,-1):
    print(palabra[x],end="")
