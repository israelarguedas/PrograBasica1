x = 0
edades = [23,45,12,21,81,14,16,20,21,10]  

for x in edades: #Todo
    print("[",x,"]",end=" ")
print("\n")

for x in range (10): #Todo
    print("[",edades[x],"]",end=" ")
print("\n")

for x in range (9,-1,-1): #Solo pares
    if (edades[x]%2 == 0):
        print("[",edades[x],"]",end=" ")