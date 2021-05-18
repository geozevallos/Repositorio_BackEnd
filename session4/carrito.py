class Product:
    precio = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    #Podemos representar este objeto como texto
    def __str__(self):
        # return self.nombre
        return f"{self.nombre} {self.precio}"

    #Retonar una operacion de igualdad entre objetos
    def __eq__(self, other):
        return self.precio == other.precio

    #Retornar una operación de comparación
    def __lt__(self, other):
        return self.precio < other.precio


class Cart:
    products = []

    #Resuelve el operador de suma:
    def __add__(self, other):
        self.products.append(other)

    def add_product(self, producto):
        self.products.append(producto)


    #ESto lo converte en una propiedad
    #Atributo o elemento calculado
    @property
    def total(self):
        total = 0
        for producto in self.products:
            total += producto.precio
        return total


iphone = Product(nombre = "iphone12", precio=5000)
macbook = Product("macbook", 8000)

cart = Cart()
cart + iphone
# cart.add_product(iphone)
# cart.add_product(macbook)

print(cart.products[0])
print(iphone == macbook)
# print(cart.total())
print(cart.total)
print(iphone > macbook)