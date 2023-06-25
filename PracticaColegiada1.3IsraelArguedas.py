#El Hotel El Sol Naciente cuenta con un precio por noche de 100 dólares. Si el usuario se 
#hospeda más de 3 noches se le aplica un porcentaje de descuento del 5% y si no se aplica 
#un porcentaje de descuento del 0%. Devuelva el monto total que debe pagar el cliente, 
#sabiendo que él indica cuántas noches se va a hospedar. 

precioPorNoche = 100
descuento = 0.95 
pagoTotal = 0

cantidadDeNoches = int(input("Ingrese la cantidad de noches que se va a hospedar:")) 

if cantidadDeNoches > 0 and cantidadDeNoches <= 3:
    pagoTotal = precioPorNoche * cantidadDeNoches
    print ("El monto por sus", cantidadDeNoches, "noches de estadia, equivale a:", pagoTotal)
elif cantidadDeNoches > 3:
    pagoTotal = precioPorNoche * cantidadDeNoches
    pagoTotal = pagoTotal * descuento
    print ("El monto por sus", cantidadDeNoches, "noches de estadia, equivale a:", pagoTotal, "dolares")
else:
    print("Ingrese un valor valido")