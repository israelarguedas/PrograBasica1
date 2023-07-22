#Desarrolle un programa para reservar espacios en una microbús que da
#servicio en 2 horarios. Se le pide que inicialmente almacene un valor 0 en
#los 10 espacios disponibles, luego le solicite al usuario la posición que
#desea reservar, remplazando el valor de 0 por un 1 (que representa
#vendido).
microbusHor1=[[0,0,0,0,0],[0,0,0,0,0]]
microbusHor2=[[0,0,0,0,0],[0,0,0,0,0]]
fila=0
columna=0
horario=0
cantEspMic01=0
cantEspMic02=0
while cantEspMic01<10 or cantEspMic02<10:
  horario=int(input("Digite el horario que desea (1 o 2):"))
  fila=int(input("Digite el número de fila:"))
  columna=int(input("Digite el número de columna:"))
  if horario==1:   
     if microbusHor1[fila][columna]==0:
        microbusHor1[fila][columna]=1
        cantEspMic01=cantEspMic01+1
     else:
        print("Espacio no disponible en microbús 1...!")
  elif horario==2:
     if microbusHor2[fila][columna]==0:
        microbusHor2[fila][columna]=1
        cantEspMic02=cantEspMic02+1
     else:
        print("Espacio no disponible en microbús 2...!")
  print("Microbús en horario 1\n____________\n")      
  for x in range(0,2):
    for y in range(0,5):
        print(microbusHor1[x][y],end=" ")
    print("\n")
  print("Microbús en horario 2\n____________\n")        
  for x in range(0,2):
    for y in range(0,5):
        print(microbusHor2[x][y],end=" ")
    print("\n")  