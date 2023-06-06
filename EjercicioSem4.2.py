distanciaKM = float(input("Ingrese la distancia en kilometro de su casa a la Universidad: "))
costoKM = float(input("Ingrese el costo por kilometro en colones: "))
diasSemana = int(input("Ingrese cuantos dias por semana visita la universidad: "))
semanasCuatrimestre = int(15)

while (diasSemana > 7): # Bucle para limitar el valor de diasSemana
    print("La cantidad de dias por semana es invalida, ingrese un numero entre 0 y 7")
    diasSemana = int(input("Ingrese cuantos dias por semana visita la universidad: "));
else:
    cantidadTotalDeDias = diasSemana * semanasCuatrimestre #Cantidad total de dias que se visita la universidad 
    costoTotalPorKm = (distanciaKM*2) * costoKM; #(distanciaKM*2) por ser ida y vuelta

Resultado = cantidadTotalDeDias * costoTotalPorKm # Resultado total en colones

print("El costo es de", Resultado, "colones, yendo", diasSemana, "dias por semana durante las 15 semanas del cuatrimestre")