print ("Bienvenido, esta es una calculadora de la formula general\n")

from math import sqrt

a= int (input ("Ingrese cuanto vale 'a': "))
b= int (input("Ingrese cuanto vale 'b': "))
c= int (input("ingrese cuanto vale 'c': "))

x1= 0
x2= 0

if (((b**2))-(4*a*c)) < 0 :
    print ("complex error")
else:
    x1= (-b+(sqrt(((b**2))-(4*a*c))))/(2*a)
    x2= (-b-(sqrt(((b**2))-(4*a*c))))/(2*a)

print ("el resultado es: \nx1=",x1, "\nx2=" ,x2)