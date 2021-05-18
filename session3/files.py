#El w es para escribir
output = open("output.txt", "w")

f = open("texto.txt", "r")


#Todo el texto
#print(f.read())


# como una linea
#print(f.readline())


#Como una lista
with f as reader:
    for line in reader:
        output.write(line[::-1])

