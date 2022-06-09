"""Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número"""

diccionario={

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}


casaca=input("Ingresa una numero pasa saber el jugador: ")
try: 
    int(casaca)
    si= True
except ValueError:
    si= False

if si == False:
    print("Debes ingresar un numero")
elif int(casaca) in diccionario:
    print(diccionario[int(casaca)])
else:
    print("lo sentimos no tenemos ese jugador ingresado")
