nombre = "Marce"
saludo = "Hola, como estas?"

# Concatenación es un proceso
# donde se pueden unir o combinar
# varias cadenas de texto
#print(saludo + " " + nombre)
print(f"{saludo} {nombre}")

menu = """
    Sistema de ingreso\n \tAcciones permitidas
    1.- Listar productos
    2.- Listar actividades
    3.- Listar empleados
    4.- C:\\Users\\Juanito\\Secreta
    5.- It\'s me
    6.- It\"s me
    Hola Mundo\r7.-
    8.- Final \b
    9.- \fFinal
"""

print(menu)

print(len(saludo))

print(saludo.upper())
print(saludo.lower())

# Inmutabilidad de strings
frase = "No me dejes nunca"
frase2 = frase.lower()
print(frase)
print(frase2)

print(frase.find("dejes"))
print(frase[6])
print(frase.replace("nunca","Bruno..."))






