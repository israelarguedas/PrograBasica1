def registroDeProductos(): 
        
    with open('Menu.txt', 'a') as f:
        f.write("\n")
        producto = f.write(input("Ingrese el nombre del producto:"))
        f.write(" | ")
        precio = f.write(input("Ingrese el precio del producto:"))
        f.write(" colones")

def impresionDeMenu(): 
    with open('Menu.txt', 'r') as f:
        f_contenidos = f.read()
        print("\n       Menu     \n",)
        print(f_contenidos, end='')    

opc = ""
while (opc != 0):
    print("\n\n   Elija entre las siguiente opciones:\n\n"
          "         Opcion 1 para ingresar un nuevo producto.\n"
          "         Opcion 2 para ver el Menu.\n")
    opc = int(input("         Ingrese su eleccion:"))

    if (opc == 1):
        registroDeProductos()
    elif (opc == 2):
        impresionDeMenu()
    elif (opc != 1) or (opc != 2):
        print("Ingrese una opcion valida")