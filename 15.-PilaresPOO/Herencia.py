class Animales():
    def habla(self):
        print("Yo soy un Animal")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))

class Perro(Animales): #asi se heredan metodos a otras clases hijas 
    pass

class Abeja(Animales):
    def __init__(self,animal):
        self.animal=animal

animal= Animales()
animal.habla()

perro=Perro() #se heredo el metodo o metodos de Animales
perro.habla()

abeja=Abeja("Abeja")
abeja.descripcion()