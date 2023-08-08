#Desarrolle una aplicación que permita almacenar números en un vector. Debe además, recorrer
#el vector e imprimir si es positivo, negativo por separado. El proceso se repetirá hasta que el
#usuario introduzca un cero. Finalmente, la aplicación debe acumular los números registrados
#divididos en positivos y negativos y debe presentar la suma total y el promedio de dichos
#números. 

numeros = []
positivos = {}
negativos = {}
sumador = 0
promedio = 0
counter = 0
n = 0
n2 = 0

opc = 1.0
while (opc != 0):
    counter = counter + 1 
    print("\n\n   Bienvenidx al sistema de diferenciacion numerica:\n")
    numeros = float(input("Ingrese los valores que desea evaluar (positivos o negativos). Si desea detenerse, ingrese 0:"))
    opc = numeros
    if (numeros > 0):
        n = n+1
        positivos[n] = numeros
 
    if (numeros < 0):
        n2 = n2+1
        negativos[n2] = numeros    

    sumador = sumador + numeros
promedio = sumador / counter

print ("Numeros positivos:", positivos)
print ("Numeros negativos:", negativos)
print ("Suma total:", sumador)
print ("Promedio total", promedio)


    
