class A():
    def __init__(self):
        self._contador = 0 #metodo correcto de encapsulamiento
        self.cuenta=0
    def incrementar(self):
        self._contador+=1
    def cuenta(self):
        return self._contador

a=A()
# print(a.cuenta)
# a.cuenta=20 #mala practica, asi no se cambia el valor de un atributo
# print(a.cuenta)


