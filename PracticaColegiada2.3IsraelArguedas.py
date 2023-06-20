#Desarrolle un programa que le solicita al usuario 15 salarios y que le indique cuánto
#dinero se necesita para que al menos todos ganen $500. 

x = 0
salario = 0

salarioFaltante = 0 
salarioMinimo = 500
salarioTotal = 0

for x in range (0,16):
    salario = int(input("Ingrese el salario: "))
    if salario < salarioMinimo:
        salarioFaltante = salarioMinimo - salario
        salarioTotal = salarioTotal + salarioFaltante

print("El monto necesario para que todos los empleados ganes al menos $500 es de:", salarioTotal)