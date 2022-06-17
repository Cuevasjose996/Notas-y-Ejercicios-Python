from traceback import print_tb


class FabricaTelefonos():
    def __init__(self,marca,color): #Constructor 
        self.marca=marca
        self.color=color
        print("El objeto {} ha sido creado".format(self.marca))

    def __str__(self):
        return "El objeto es {}".format(self.marca) #Llama a un atributo del objeto o str marcado.

    def __del__(self): #Destructor
        print("El objeto {} ha sido destruido".format(self.marca)) 


telefono=FabricaTelefonos("Nokia", "Negro")

print(telefono.marca)
print(telefono)