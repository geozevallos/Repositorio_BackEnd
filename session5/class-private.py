class Empleado:

    __salario = 0

    def __init__(self, nombre, salario):
        self.__salario = salario
        self.nombre = nombre

    def __calcular_salario(self):
        return self.__salario

    def pagar(self):
        monto = self.__calcular_salario()
        print(f'{monto} pagado')


jose = Empleado("Jose Salazar",salario = 400)

# print(jose.__salario)
print(jose.nombre)
print(jose.pagar())

# print(dir(jose))

print(jose._Empleado__salario)