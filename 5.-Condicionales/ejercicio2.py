"""Escribir un programa que, dado un numero entero, 
muestre su valor absoluto. Nota: para los numeros 
positivos su valor absoluto es igual al numero, mientras que para los negativos, 
su valor es el numero multiplicado por el -1"""

numero= int(input("ingresa un numero entero: "))

if numero >=0:
    print("El valor absoluto es: ",numero)
else:
    print("El valor absoluto es: ",numero*-1)