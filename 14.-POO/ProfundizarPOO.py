class FabricaTelefonos():
    def __init__(self,marca, *colores, **modelos): #se pueden agregar tuplas y diccionarios como atributos
        self.marca=marca
        self.colores=colores
        self.modelos=modelos


telefono= FabricaTelefonos("alcatel", "negro", "azul", "rojo", m1=500, m2=1000)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

telefono.memoria=512
print(telefono.memoria) #atributo temporal