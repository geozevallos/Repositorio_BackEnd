class Student:

    def __init__(self, nombre):
        self.__notas= []
        self.nombre = nombre

    def get_notas(self, indices):
        nota = self.__notas[indices]
        if nota > 11:
            return nota
        else:
            raise Exception("Usted no puede ver eesa nota")

    def set_notas(self, nota):
        if len(self.__notas) >= 3:
            # raise para lanzar un error
            raise Exception ("Todas las notas han sido registradas")
        else: self.__notas.append(nota)
    
    @property
    def promedio(self):
        sum = 0.0
        cantidad = 0.0
        for nota in self.__notas:
            sum += nota
            cantidad +=1
        
        return sum / cantidad


alumno1 = Student("Jaimito")
alumno1.set_notas(10)
alumno1.set_notas(15)
alumno1.set_notas(8)

print(alumno1.promedio)
print(alumno1.get_notas(0))