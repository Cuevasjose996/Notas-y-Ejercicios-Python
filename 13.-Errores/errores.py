while True: #bucle para repetir la pregunta
    try:
        edad=int(input("ingrese su edad: "))
        print("Tu edad es: ", edad)
        break #terminar bucle
    except: #mensaje de error
        print("ingresaste un valor erroneo")
    finally:
        print("la ejecucion ha finalizado")