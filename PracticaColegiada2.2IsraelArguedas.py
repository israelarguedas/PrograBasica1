#Desarrollar un programa que le solicite al usuario un valor y muestre los primeros
#10 números divisibles entre este valor. 

valor = 0
numeroDivisible = 1
divisores = 0
valor = int(input("Ingrese el valor: "))

while (divisores <= 10):
    if (numeroDivisible%valor == 0):
        divisores+=1
        print("El numero", valor, "es divisor del numero", numeroDivisible)
    numeroDivisible+=1

        

