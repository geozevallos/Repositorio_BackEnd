class Curso:
    nombre = "Matemática"
    __notas = []
    promedio = 0

    def set_notas(self, nota):
        self.__notas.append(nota)
    
    
    


class Alumnos:
    def __init__(self, nombre):
        self.nombre = nombre

    