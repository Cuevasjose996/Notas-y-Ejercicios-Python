"""Crear una funcion que pida dos numeros. 
Si el primero es mayor al segundo, el programa debe retornar el valor 1;
si el segundo es mayor al primero, debe retornar -1; 
si ambos son iguales, debe retornar 0"""



def resultado():
    valor1=int(input("Ingrese el valor 1: "))
    valor2=int(input("Ingrese el valor 2: "))
    if valor1>valor2:
        return 1
    elif valor1<valor2:
        return -1
    else:
        return 0

print(resultado())
