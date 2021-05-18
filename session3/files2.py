rango = list(range(1,1000))

str_range = []

for i in rango:
    str_range.append("numero : \t" + str(i) + "\n")

output = open("output2.txt", "w")

output.writelines(str_range)