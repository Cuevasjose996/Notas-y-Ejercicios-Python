from traceback import print_tb


diccionario= {1:2,2:3,3:4}
diccionario2= {4:5,6:7}

print(diccionario)

"""diccionario.pop(3) #metodo para eliminar una clave y su contra
print(diccionario)"""

'''diccionario.clear() #metodo para limpiar todo el diccionario
print(diccionario)'''

"""print(diccionario.get(2))""" #get trae valores

"""diccionario.setdefault(4,5) #agrega una llave y su contrasenia al final
print(diccionario)"""

"""diccionario.update(diccionario2) #Actualiza un diccionario agregandole datos
print(diccionario)"""

diccionario.copy() #genera una copia del diccionario
print(diccionario)