numero= int(input("ingrese un valor numerico: "))

i= 0
multi=0

while numero>=0 and i<=10:
    multi=numero*i
    print(' {} x {} = {} '.format(numero,i,multi))
    i +=1