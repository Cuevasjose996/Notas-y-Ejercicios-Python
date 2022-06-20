
class Marino():
    def hablar(self):
        return "Hola..."

class Pulpo(Marino):
    def hablar(self):
        return "Soy un pulpo"

class Foca(Marino):
   def hablar(self,mensaje):
    self.mensaje=mensaje
    return self.mensaje

marino=Marino()
print(marino.hablar())

pulpo=Pulpo()
print(pulpo.hablar())

foca=Foca()
print(foca.hablar("Soy una foca"))