#Escriba un programa que solicite un numero.
#Genere la tabla de multiplicar ese numero.

numero = 0
x = 0
resultado = 0
numero = int(input("Ingrese el numero de su tabal de multiplicar: "))
tabla: numero+1

for x in range (0,13):
    resultado = numero*x    
    print(numero,"x", x,"=",resultado)