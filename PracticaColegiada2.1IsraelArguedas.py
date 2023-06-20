#Se requiere analizar las estaturas de los N niños de una escuela y extraer la siguiente estadística:
    #• Cantidad de niños que miden menos de 100 cm.
    #• Cantidad de niños que miden entre 100 y 120 cm.
    #• Cantidad de niños que miden entre 121 y 130 cm.
    #• Cantidad de niños que miden entre 131 y 140 cm.
    #• Cantidad de niños que miden más de 140 cm.
    #• Promedio de estaturas.
    #• Muestre los resultados obtenidos.

cantidadNiños = 0
estatura = 0
niñosBajo100 = 0
niñosEntre100y120 = 0
niñosEntre121y130 = 0
niñosEntre131y140 = 0
niñosSobre140 = 0
promedioEstaturas = 0
continuar = "s"

while continuar == "s":
    estatura = float(input("Ingrese la estatura del estudiante: "))
    cantidadNiños+=1

    if (estatura<100):
        niñosBajo100+=1
        promedioEstaturas = promedioEstaturas + estatura

    elif (estatura >= 100 and estatura <= 120):
        niñosEntre100y120+=1
        promedioEstaturas = promedioEstaturas + estatura

    elif (estatura >= 121 and estatura <= 130):
        niñosEntre121y130+=1
        promedioEstaturas = promedioEstaturas + estatura

    elif (estatura >= 131 and estatura <= 140):
        niñosEntre131y140+=1
        promedioEstaturas = promedioEstaturas + estatura

    elif (estatura>140):
        niñosSobre140+=1
        promedioEstaturas = promedioEstaturas + estatura
    
    continuar = input("Desea ingresar otra estatura (s/n)?")
        

promedioEstaturas = promedioEstaturas/cantidadNiños

print("La cantidad de niños que miden menos de 100 cm es:", niñosBajo100)
print("La cantidad de niños que miden entre 100 y 120 cm es:", niñosEntre100y120)
print("La cantidad de niños que miden entre 121 y 130 cm es:", niñosEntre121y130)
print("La cantidad de niños que miden entre 131 y 140 cm es:", niñosEntre131y140)
print("La cantidad de niños que miden más de 140 cm es:", niñosSobre140)
print("El promedio de estaturas equivale a:", promedioEstaturas)
