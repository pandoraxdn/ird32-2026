valor = int(input())

lista = []

for element in range(1,valor+1):
    if element % 2 == 0:
        lista.append(element)

print(lista)
