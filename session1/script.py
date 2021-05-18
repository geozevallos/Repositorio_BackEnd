print("Ingrese edad")
edad = input()

if int(edad) > 18:
    print("es mayor de edad")
elif int(edad) < 0:
    print("edad invalida")
else:
    print("no es mayor de edad")