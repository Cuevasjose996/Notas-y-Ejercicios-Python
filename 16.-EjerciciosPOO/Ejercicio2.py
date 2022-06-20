class Calculadora():
    def __init__(self):
        self.numero1= int(input("Ingresa un numero: "))
        self.numero2= int(input("Ingresa un segundo numero: "))

    def suma(self):
        self.suma=self.numero1+self.numero2
        return "la suma es: {}".format(self.suma)
    
    def resta(self):
        self.resta=self.numero1-self.numero2
        return "la resta es: {}".format(self.resta)
    
    def mult(self):
        self.mult=self.numero1*self.numero2
        return "la multiplicacion es: {}".format(self.mult)
    
    def div(self):
        if self.numero1==0:
            return "Error no se puede dividir Cero"
        elif self.numero2==0:
            return "Indeterminacion"
        else:
            self.div=self.numero1/self.numero2
            return "la division es : {}".format(self.div)

calcular =Calculadora()
print(calcular.suma())
print(calcular.resta())
print(calcular.div())
print(calcular.mult())



