def valores():
    global num1 #Convierte las variables de una funcion en variables globales
    global num2 #Convierte las variables de una funcion en variables globales
    num1=110
    num2=40
    resultado= num1+num2
    return resultado

print(valores())

resta=num1-num2
print(resta)