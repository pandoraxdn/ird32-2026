lista = [1,2,3,4,5,6]
frase = "No me dejes nunca Natasha"
lista_vacia = []
print(lista)

for element in lista:
    print(element)

for element in frase:
    if element != " ":
        lista_vacia.append(element)

print(lista_vacia)

lista_vacia = []
for element in range(0,1000000):
    numero = element ** 2
    if numero % 3 == 0:
        lista_vacia.append(element)

print(lista_vacia)
print(len(lista_vacia))
