class Fabrica():
    def __init__(self, llantas, color,precio ):
        self.llantas=llantas
        self.color=color
        self.precio=precio


class Carro(Fabrica):
    def datos(self):
        print("La cantidad de llantas del carro es de: {}".format(self.llantas))
        print("El color del carro es: {}".format(self.color))
        print("El precio del carro es: $ {}".format(self.precio))

class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas de la moto es: {}".format(self.llantas))
        print("El color de la moto es: {}".format(self.color))
        print("El precio de la moto es: $ {}".format(self.precio))

moto=Moto(2,"negro", 4000)
moto.datos()

carro= Carro(4,"azul", 20000)
carro.datos()