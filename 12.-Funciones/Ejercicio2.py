"""Escribir una función que reciba un 
número entero positivo y devuelva su factorial."""

def factorial():
    numero=int(input("Escribe un numero entero positivo: "))
    if numero>0:
        fac=1
        for i in range(1,numero+1):
            fac=fac*i
        print(fac)
    else:
        print("el numero es negativo")

factorial()

