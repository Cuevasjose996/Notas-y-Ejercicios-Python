#Escribir un programa que le pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad= int(input("Cual es tu edad?: "))

i= 0

while 0<edad and i-edad != 0:
    print("haz cumplido {} años".format(i+1))
    i += 1
