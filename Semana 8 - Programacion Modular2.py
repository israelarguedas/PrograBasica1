nombre = ""

def leerNombre():
    nombre=input("Dime tu nombre:")
    return nombre

def saludar(nombre):
    print("Hola", nombre,"es un gusto")

nombre = leerNombre()
saludar(nombre)