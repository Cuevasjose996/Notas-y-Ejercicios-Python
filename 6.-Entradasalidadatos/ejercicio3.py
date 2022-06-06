'''Escribir un programa que solicite al usuario un vocal minuscula, 
y luego una letra mayuscula. El programa debe convertir la letra 
minuscula y la vocal mayuscula, y al final deben ser concatenadas
ambas'''

print("Este programa convierte letras minusculas y mayusculas")

import string
def listAlphabet():
    return list(string.ascii_uppercase)

vocalminuscula= input("ingresa una vocal: ")
if vocalminuscula in ("a", "e", "i", "o", "u"):
    print("Su letra es: ", vocalminuscula) 
else:
    print ("Caracter no valido")

lmayusc= input("ingrese una letra mayuscula :")
if lmayusc in listAlphabet():
    vocalminuscula_upper=vocalminuscula.upper()
    lmayusc_lower=lmayusc.lower()
    print("El resultado de la conversion es:\n" ,vocalminuscula_upper, "\nY:\n", lmayusc_lower)
else:
    print("Caracter no valido")
