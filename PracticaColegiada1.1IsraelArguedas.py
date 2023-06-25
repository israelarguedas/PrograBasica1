#La Fábrica de Chocolates El Tesoro de los Dulces requiere realizar un aumento a sus colaboradores 
#según el tiempo de antigüedad en la empresa. Para ello utiliza los siguientes criterios:

#Antigüedad         % Aumento       Tier
#- De 0 a 5 años        10%         tier1
#- De 6 a 9 años        15%         tier2
#- De 10 a 15 años      25%         tier3
#- Mäs de 15 años       30%         tier4

#Cree un programa que solicite el salario actual y el tiempo de laborar en años, calcule el 
#aumento y el nuevo salario y muestre la información calculada. 

tier1 = 1.10
tier2 = 1.15
tier3 = 1.25
tier4 = 1.30

tiempoLaborado = int(input("Ingrese la cantidad de años laborados en la empresa:")) 
salarioActual = float(input("Ingrese su salario actual:")) 

if (tiempoLaborado >= 0 and tiempoLaborado <= 5):
    salarioActual = salarioActual * tier1
    print("El salario con el incremento equivale a:", salarioActual)
elif (tiempoLaborado >= 6 and tiempoLaborado <= 9):
    salarioActual = salarioActual * tier2
    print("El salario con el incremento equivale a:", salarioActual)
elif (tiempoLaborado >= 10 and tiempoLaborado <= 15):
    salarioActual = salarioActual * tier3
    print("El salario con el incremento equivale a:", salarioActual)
elif (tiempoLaborado > 15):
    salarioActual = salarioActual * tier4
    print("El salario con el incremento equivale a:", salarioActual)
else:
    print("Ingrese un valor valido")
    

