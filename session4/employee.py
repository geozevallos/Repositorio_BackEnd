class Empleado:

    #Esto es un atributo por defecto
    numero_ventas = 0

    #Al crear un objeto debe pedir estos datos

    def __init__(self, nombre, apellido, salario, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.dni = dni
    
    #Para que sea accesible desde una instancia, colocamos el self
    def vender(self):
        self.numero_ventas =+ 1
        print(f"{self.nombre} hizo una venta :D")
    
    def reportar(self):
        print(f"{self.nombre} hizo {self.numero_ventas} venta(s)")




jorge = Empleado("Jorge", "Zevallos", 10000, "4343443")
maria = Empleado("Maria", "Rivera", 100, "4378443")
jorge.vender()
jorge.reportar()
maria.vender()
maria.reportar()
