# class FabricaTelefonos():
#     marca= "samsung"

#     def ElaborarHuawei(self):
#         self.marca="Huawei"

# telefono=FabricaTelefonos()
# telefono.ElaborarHuawei()
# print(telefono.marca)

class FabricaTelefonos():
    def __init__(self,marca,color):
        self.marca=marca
        self.color=color
        
telefono=FabricaTelefonos("Huawei", "Verde")
print(telefono.marca)
print(telefono.color)