
def sumar():
    num1 = int(input("Ingrese el primer numero:"))
    num2 = int(input("Ingrese el segundo numero:"))
    suma = num1 + num2
    print("La suma es:", suma)

def restar():
    num1 = int(input("Ingrese el primer numero:"))
    num2 = int(input("Ingrese el segundo numero:"))
    resta = num1 - num2
    print("La resta es:", resta)

def multiplicar():
    num1 = int(input("Ingrese el primer numero:"))
    num2 = int(input("Ingrese el segundo numero:"))
    multiplicacion = num1 * num2
    print("La multiplicacion es:", multiplicacion)

def dividir():
    num1 = int(input("Ingrese el primer numero:"))
    num2 = int(input("Ingrese el segundo numero:"))
    division = num1 / num2
    print("La division es:", division)

opc = 0
while (opc!=5):
    opc=int(input("\nMenu de calculadora\n\n"
    "1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n\n"
    "Digite su opcion:"))
    if(opc==1):
        sumar()
    elif(opc==2):
        restar()
    elif(opc==3):
        multiplicar()
    elif(opc==4):
        dividir()
    elif(opc==5):
        print("Hasta luego!")
        quit()
    else:
        print("Ingrese una opcion valida")


