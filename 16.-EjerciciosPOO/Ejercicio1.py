class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):
        print("nombre: {}\nNota: {}".format(self.nombre,self.nota))

    def resultados(self):
        if self.nota<7:
            print("Haz REPROBADO")
        else:
            print("Has APROBADO")

estudiante1=Estudiante("Daniel",10)

estudiante1.imprimir()
estudiante1.resultados()