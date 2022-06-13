#Escribir una funcion que reciba una muestra de numeros en una tupla y devuelva su medida.

def medida(*muestra):
    print(len(muestra))

medida(2,545,5,6,78,5)

def medida(*tupla):
    return len(tupla)

print(medida(5,4,5,7,9,5,1))