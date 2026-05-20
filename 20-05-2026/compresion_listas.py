numeros = [1,2,3,4,5,6,7,8,9]

cuadrados = [ element ** 2 for element in numeros ]

print(cuadrados)

numeros = range(1,1000001)

lista = [ element for element in numeros if element % 3 == 0 ]

print(len(lista))

sumatoria = [ element for element in range(0,101) ]
print(sum(sumatoria))
