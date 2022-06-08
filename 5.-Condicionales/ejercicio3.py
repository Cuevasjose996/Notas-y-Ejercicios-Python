"""Escribe un programa que pida dos palabras y diga si rima o no.
si coinciden las tres ultimas letras tiene que escribir 'riman'
si coinciden las ultimas 2 'rima un poco' y si no, que no riman"""

palabra1= input("Ingrese palabra 1: ")
palabra2= input("ingrese palabra 2: ")

ultimas31=palabra1[-3:]
ultimas32=palabra2[-3:]
ultimas21=palabra1[-2:]
ultimas22=palabra2[-2:]

if len(palabra1)<3 or len(palabra2)<3:
    print("No riman, hay una palabra con 2 o menos letras")
elif ultimas31.lower() == ultimas32.lower():
    print("las palabras riman")
elif ultimas21.lower() == ultimas22.lower():
    print("las palabras riman un poco")
else:
    print("las palabras no riman")