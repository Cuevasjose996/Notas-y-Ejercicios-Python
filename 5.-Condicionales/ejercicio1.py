"""Crea un programa que pida al usuario una letra, y si es una vocal,
muestre el mensaje "es vocal". Sino, decirle al usuario que no es vocal"""

letra= (input("ingresa una letra: "))

if letra.lower() in "aeiou":
    print("Tu letra es una vocal")
else:
    print ("tu letra no es una vocal.")