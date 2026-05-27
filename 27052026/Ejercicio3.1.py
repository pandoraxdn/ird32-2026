def factorial(numero):
    total = 1
    for element in range(numero,1,-1):
        total *= element
    print(total)
    
valor = int(input())
factorial(valor)