class Animal:

    nombre = "animal"

    def __init__(self, nombre):
        self.nombre = nombre
    
    def dormir(self):
        print("zzz")


#Heredando
class Dog(Animal):
    
    def ladrar(self):
        print("wau wau")


class Cat:
    
    def maullar(self):
        print("miau")


duqueza = Dog("Duqueza")
duqueza.dormir()
duqueza.ladrar()
print(duqueza.nombre)