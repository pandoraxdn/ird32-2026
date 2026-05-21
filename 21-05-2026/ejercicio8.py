palabra = input()

contador = 0
vocales = [ "a", "e", "i", "o", "u" ]

for element in palabra:
    if element in vocales:
        contador+=1

print(contador)
