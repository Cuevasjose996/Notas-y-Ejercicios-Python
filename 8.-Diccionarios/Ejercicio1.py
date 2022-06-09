"""En el siguiente diccionario se encuentran capitales de los paises en el mundo,
debes realizar un programa que pida un pais al usuario, y muestre
la capital de ese pais, en dado caso el pais no este en el diccionario, 
se debe mostrar el mensaje 'no se encuentra'"""



capitalespaises= {"Guatemala": "Ciudad de Guatemala", "El salvador":"San Salvador", "Honduras":"Tegucigalpa", "Nicaragua":"Managua", "Costa rica":"San Jose", "Panama":"Panama", "Argentina": "Buenos aires", "Colombia":"Bogota", "Venezuela":"Caracas", "España":"Madrid"}

paisseleccion= input("Ingresa un pais: ")
letra= paisseleccion.capitalize() in capitalespaises

if letra== True:
    print(capitalespaises[paisseleccion.capitalize()])
else:
    print("El pais no se encuentra en el diccionario")

