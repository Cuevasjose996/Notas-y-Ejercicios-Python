from pdb import pm


print("Este programa te muestra tu promedio")

p1= input("Ingrese la calificacion de la primera practica: ")
p1= float (p1)
p2= input("Ingrese la calificacion de la segunda practica: ")
p2= float (p2)
p3= input("Ingrese la calificacion de la tercera practica: ")
p3= float (p3)

pp= (p1+p2+p3)/3

ep= input("ingrese la calificacion del examen parcial: ")
ep= float (ep)

ef= input("ingrese la calificacion del examen final: ")
ef= float (ef)

prom= (pp+ 2*ep+ 3*ef)/6

print("El promedio de practicas es de:\n ", pp, "\n Y el promedio final es de:\n", prom)
    