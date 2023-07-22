calificaciones=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,5):
 for y in range(0,3):
   calificaciones[x][y]=int(input("Digite la calificación del estudiante:"))
for x in range(0,5):
 for y in range(0,3):
   print(calificaciones[x][y],end=" ")
 print("\n")  
