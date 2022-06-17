class Fabricatelefonos():
    marca="Huawei"
    color="Negro"
    MemoriaRam=32
    Almacenamiento= 128
    def llamar(self,mensaje):
        return mensaje
    
    def EscucharMusica(self):
        print("Estas escuchando Musica")


telefono=Fabricatelefonos()
telefono.marca
print(telefono.marca)
telefono.color
telefono.MemoriaRam
telefono.Almacenamiento
print(telefono.Almacenamiento)

print(telefono.llamar("Hola, con quien hablo?"))
telefono.EscucharMusica()