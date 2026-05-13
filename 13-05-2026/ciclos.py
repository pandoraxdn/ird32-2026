"""
contador = 1

while contador <= 100:
    print(contador)
    contador+=1

contador = 100

while contador > 0:
    print(contador)
    contador-=1

for element in range(0,101,1):
    print(element)

for element in range(100,0,-1):
    print(element)
"""

menu = """
    Menú de calculadora
    Acciones
        1.- Sumar
        2.- Restar
        3.- División
        4.- Multiplicación
        5.- Salir
"""

while True:
    print(menu)
    accion = int(input("Acción: "))
    if accion == 5:
        break
    valor1 = int(input("Ingresa valor 1: "))
    valor2 = int(input("Ingresa valor 2: "))
    
    if accion == 1:
        print(f"Resultado: {valor1+valor2}")
    elif accion == 2:
        print(f"Resultado: {valor1-valor2}")
    elif accion == 3:
        print(f"Resultado: {valor1/valor2}")
    elif accion == 4:
        print(f"Resultado: {valor1*valor2}")
