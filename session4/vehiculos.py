class motor:
    tipo= ""

class timon:
    color = "negro"

class espejos:
    material = "Vidrio"

class llantas: 
    material = "caucho"

class car:
    motor = motor()
    timon = timon()
    espejos = [espejos(), espejos(), espejos()]
    llantas = [llantas(), llantas(), llantas(), llantas()]

class motocicleta:
    motor = motor()
    espejos = [espejos(), espejos()]
    llantas = [llantas(), llantas()]

nissan = car()
print(nissan.llantas)

kawasaki = motocicleta()
print(motocicleta.llantas)