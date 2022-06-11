'''Pedir al usuario que ingrese 2 numeros, después,
se debe mostrar el rango de esos 2 números, pero,
solo imprimiendo los números que sean impares'''

numero1= int(input("ingrese un valor: "))
numero2= int(input("ingrese otro valor: "))

tipo=(numero1%2)
tipo2=(numero2%2)


if numero1<numero2 and tipo==1:
    for i in range(numero1,numero2+1,2):
        print(i)
elif numero1<numero2 and tipo==0:
    for i in range(numero1+1,numero2+1,2):
        print(i)
elif numero1>numero2 and tipo2==1:
    for i in range(numero2,numero1+1,2):
        print(i)
elif numero1>numero2 and tipo2==0:
    for i in range(numero2+1,numero1+1,2):
        print(i)
else:
    print("ingrese un valor valido")


#otra solucion mas sencilla

num3= int(input("ingresa el primero numero: "))
num4= int(input("ingresa el segundo numero: "))

if num3<num4:
    for j in range(num3, num4+1):
        if j%2==0:
            continue
        print(j)
elif num3>num4:
    for j in range(num4, num3+1):
        if j%2==0:
            continue
        print(j)
else:
    print("ingrese un valor valido")