#Se ha decidico aplicar un porcentaje adicional a la nota final 
#de un estudiante segun el siguiente criterio: 
#Si la nota esta entre 100 y 80 se le aplicar un 5%, si esta
#entre 79 y 75 se le aplicara un 3%, si esta entre 74 y 70,
#se le aplicara un 2%. En cualquier otro caso la nota permanecera
#igual. Escriba un prgrama que lea la nota actual y determine
#la nueva nota.

notaFinal = 0
nuevaNota = 0 
notaFinal = float(input("Ingrese la nota final: "))

if notaFinal >=80 and notaFinal <=100:
    nuevaNota = notaFinal * 1.05 
elif notaFinal >=75 and notaFinal <=79:
    nuevaNota = notaFinal * 1.03
elif notaFinal >=70 and notaFinal <=74:
    nuevaNota = notaFinal * 1.02
else:
    nuevaNota = notaFinal

print("La nota original equivale a:", notaFinal,
"\nla nota final equivale a:", nuevaNota)
