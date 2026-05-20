
def saludo():
    print("Saludo")

saludo()

def sumar(a, b):
    return a + b

print(sumar(10,20))
print(sumar(10,30))

def imprimir( nombre, apellido="", edad=0 ):
    if edad != 0:
        print(f"Saludos: {nombre} {apellido}, edad: {edad}")
    else:
        print(f"Saludos: {nombre} {apellido}")

imprimir("Rodrigo","Rojas")
imprimir("Natalia","Rojas",37)

def sumar_n(*argumentos):
    resultado = 0
    for element in argumentos:
        resultado+=element
    print(resultado)

sumar_n(10,10)
sumar_n(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

# !5 = 5 x 4 x 3 x 2 x1 = 120
# Funciòn recursiva
def factorial(numero):
    if numero == 1:
        return 1
    else:
        factorial_parcial = numero * factorial(numero - 1)
        return factorial_parcial

print(factorial(5))





