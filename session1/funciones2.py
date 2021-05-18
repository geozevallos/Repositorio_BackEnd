#Recibiendo muchos parámetros

#El asterisoc especifica que searan varios parametros
#Con un * se imprimira una tupla, con2 un diccionario
# def imprimir_numeros(**n):
#     print(n)

# imprimir_numeros(
#     name = "Jorge",
#     apellido = "Zevallss",
#     edad = "20"
# )

#Texto al reves -------------------

# def revert2(text):
#     final = ""
#     for char in text:
#         final = char + final
#     return final

# print(revert2("Jorge"))

# Palindrome -------------------------------
# def palindroma(text):
#     final = ""
#     for char in text:
#         final = char + final
    
#     if(text == final):
#         return True
#     else: return False

# print(palindroma("ACCA"))

#Otra manera
# def reverse(text):
#     return text[::-1]

# def isPalindrome(text):
#     return text == reverse(text)

# print(isPalindrome("ABCBA"))

## ADN ------------------------------
# ADN2 = {"T": "A", "A": "T", "C":"G", "G":"C"}

# def ADN(secuencia):
#     for i in secuencia:
#        for j in ADN2.keys():
#            if(i == j):
#                return ADN2[f'{i}']


# print(ADN("TAC"))

def get_complement(seq_adn):
    dict_complements = {"T": "A", "A": "T", "C":"G", "G":"C"}
    complement = ""
    for e in seq_adn:
        complement += dict_complements[e]
    
    return complement

print (get_complement("TACG"))