"""Crear un programa que tenga una lista, 
luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. 
Debes crear una segunda funcion en donde se ordenen 
los numeros pares e impares dentro de dos listas nuevas"""

lista=[]

def llenado():
    i=1
    while i<=10:
        agregar = int(input("Ingresa un numero para agregar a la lista: "))
        lista.append(agregar)
        i=i+1
    print(lista)

def orden():
    listapares=[]
    listaimpares=[]
    for j in lista:
        if j%2==0:
            listapares.append(j)
        else:
            listaimpares.append(j)
    listapares.sort()
    listaimpares.sort()
    print("la lista impares es:",listaimpares)
    print("la lista pares es:",listapares)

llenado()
orden()