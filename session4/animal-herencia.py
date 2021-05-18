class Mamifero:
    def nadar(self):
        print("Nadando como un mamifero")


class Pez:
    def nadar(self):
        print("Nadando...")


#pass es q no va hacer nada
class Delfin(Pez, Mamifero):
    pass

class Mono(Mamifero):
    pass

#Saber el orden de ejecucion
print(Delfin.__mro__)

# chita = Mono()
# flipper = Delfin()

# chita.nadar()
# flipper.nadar()
