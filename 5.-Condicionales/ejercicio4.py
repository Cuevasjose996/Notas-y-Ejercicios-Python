"""Crea y programa que permita al usuario elegir un candidato por el cual votar.
Las posibilidades son Candidato 'A' por el partido rojo,
Candidato 'B' por el partido verde, Candidato 'C' por el partido azul.
Segun el candidato elegido (A,B o C) se le debe imprimir el mensaje
'Usted ha votado por el partido [color que corresponda]. Si el usuario ingresa
una opcion que no corresponde a ninguno de los candidatos posibles, indicar 'opcion erronea'"""

print("Bienvenido a las votaciones, los candidatos son:\nMenganito Perez: Opcion 'A' (partido Rojo)\nPeregrina Mendoza: Opcion 'B' (partido Verde)\nAgustin Valdez: Opcion 'C' (partido Azul)")

seleccion= (input("Porfavor, Ingresa la letra del candidato que deseas votar: "))

if seleccion.upper() == "A":
    print("Haz votado por el color Rojo")
elif seleccion.upper() == "B":
    print("Haz votado por el color Verde")
elif seleccion.upper() == "C":
    print("Haz votado por el color Azul")
else: 
    print("Opcion erronea")