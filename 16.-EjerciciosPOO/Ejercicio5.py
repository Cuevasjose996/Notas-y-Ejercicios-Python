class Universidad():
    def __init__(self,Nombre):
        self.Nombre=Nombre

class Carrera():
    def carrera(self,especialidad):
        self.especialidad=especialidad

class Estudiante(Universidad,Carrera):
    def datos(self,nombre, edad):
        self.nombre= nombre
        self.edad=edad
        print("Mi nombre es{}, tengo {} años, mi especialidad es {}. Estudio en la Universidad {}. ".format(self.nombre,self.edad,self.especialidad,self.Nombre))

persona=Estudiante("Instituto tecnologido de tijuana")
persona.carrera("Sistemas")
persona.datos("Jose Cruz", 25)
