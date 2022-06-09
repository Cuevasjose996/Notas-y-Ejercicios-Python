'''Escribe una lista que tenga los numeros del 1 al 10.
luego, debes hacer que los datos que estan en las posiciones 4,7 y 9
sean multiplicados por 2; por ultimo. mostrar la nueva lista con los nuevos datos'''

lista= [1,2,3,4,5,6,7,8,9,10]
print("La lista va a ser transformada: \n", lista)

lista[3]=lista[4]*2
lista[6]=lista[6]*2
lista[8]=lista[8]*2

print(lista)

