'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''

tupla=("enero","febrero","marzo","abril", "mayo", "junio", "julio", "agosto", "septiembre","octubre", "noviembre","diciembre")

dato= input("ingresa un numero del 1 al 12: " )


try: 
    int(dato)
    si= True
except ValueError:
    si= False

if si==False:
    print("ingresa un dato valido")
elif si==True:
    dato=int(dato)
    if 1<=dato<=13:
        dato -= 1
        print("Tu mes es: ", tupla[dato])
    else:
        print("ingresa un valor valido")
else:
        print("ingresa un valor numerico")

