# Map
lista = [21, 3, 5, 65, 12]

def nx2 (n):
    return n * 2

mapa = map(nx2, lista)

print(mapa)
print(list(mapa))


#Filter

def esAdulto (x):
    return x > 18


filtrada = filter(esAdulto, lista)
print(filtrada)
print(list(filtrada))


#Funciones lambda

isAdult = lambda x: x>18

print()