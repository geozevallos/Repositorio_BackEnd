class Pet:

    def __init__(self, nombre):
        self.nombre = nombre


    def alimentar(self):
        print("Alimentacion generica")
    


class Dog(Pet):
    def alimentar(self):
        print("dar croquetas")

class Cat(Pet):
    def alimentar(self):
        print("dar enlatado")

class Turtle(Pet):
    pass

mascotas = [
    Dog(nombre = "Duke"),
    Cat(nombre = "Silvestre"),
    Turtle(nombre = "Donatello")
]

for mascota in mascotas:
    mascota.alimentar()