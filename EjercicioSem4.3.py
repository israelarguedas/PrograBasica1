ladoCuadrado = float(input("Ingrese la medida del lado del cuadrado en centrimetros: "))
cantidadDeLados = 4

perimetro = ladoCuadrado * cantidadDeLados # Lado por 4(cantidad de lados)
area = ladoCuadrado ** 2 # Lado elevado al cuadrado

print("El perimetro del cuadrado es:", perimetro, "centrimetros")
print("El area del cuadrado es:", area, "centrimetros")