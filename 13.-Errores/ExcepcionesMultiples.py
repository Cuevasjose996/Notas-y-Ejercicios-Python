while True:
    try: 
        num1=int(input("ingresa un numero: "))
        resultado=100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("no se puede dividir entre cero")

while True:
    try:
        edad=int(input("ingresa tu edad: "))
        print("tu edad es: ", edad)
        break
    except ValueError:
        print("has colocado un valor erroneo")

while True:
    try: 
        edad=int(input("ingresa tu edad: "))
        print("tu edad es: ", edad)
        break
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecucion")
        break
