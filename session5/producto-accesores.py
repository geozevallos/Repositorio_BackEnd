'''
class Product:

    def __init__(self, costo):
        self.__costo = costo
        self.__precio = self.__costo * 1.57

    
    def getPrecio(self, descuento):
        return self.__precio * (1-descuento)

play5 = Product(3000)

precio = play5.getPrecio(0.10)

print(precio)
'''

class Product:

    descuento = 0.1

    def __init__(self, costo):
        self.__costo = costo
        self.__precio = self.__costo * 1.57

    @property
    def precio_final(self, descuento):
        return self.__precio * (1-descuento)

play5 = Product(3000)
print(play5.precio_final)
