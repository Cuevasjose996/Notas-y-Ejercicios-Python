"""En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
a su vez, debe pedir dos datos y esos que sean ingresados
deben ser suistituidos en el primer y segundo lugar"""

lista= [20,50,"curso", "python", 3.14]
print("Estos son los valores de la lista:\n", lista)

lista[0]= input("Ingresa un valor:")
lista[1]= input("ingresa un segundo valor: ")

print(lista)