class Dog:

    nombre = "perro"

    def __init__(self, nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print("wau wau")
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    


fido = Dog(nombre="Fido")
Duqueza = Dog(nombre="Duqueza")

print(Duqueza.nombre)
fido.ladrar()