'''Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y 
mostrar el rango de numeros entre ambas cifras'''


for i in range (1,11):
    print(i)

valor1=input("ingresa un valor: ")
valor2=input("ingresa otro valor: ")

try: 
    int(valor1) and int(valor2)
    si= True
except ValueError:
    si= False

if si==False:
    print("ingresa un dato valido")
elif si==True and valor1<valor2:
    valor1=int(valor1)
    valor2=int(valor2)
    for j in range(valor1,valor2+1):
            print(j)
elif si==True and valor1>valor2:
    valor1=int(valor1)
    valor2=int(valor2)
    for k in range(valor2,valor1+1):
        print(k)
else:
    print("datos ingresados no validos")