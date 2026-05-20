from Empleado import Empleado
from Disenador import Disenador

menu = """
    Bienvenido al sistema de Empleados
        1.- Crear Empleado
        2.- Crear Diseñador
        3.- Listar Registros
        4.- Salir
"""

lista = []

while True:
    print(menu)

    opcion = int(input("Ingresa una acciòn: "))

    if opcion == 4:
        break

    if opcion == 3:
        for element in lista:
            print(element)

    nombre = input("Nombre del empleado: ")
    apellido_p = input("AP del empleado: ")
    apellido_m = input("AM del empleado: ")
    edad = input("Edad del empleado: ")
    no_empleado = int(input("NoEmp del empleado: "))
    salario = float(input("Salario del empleado: "))

    if opcion == 1:
        empleado = Empleado(nombre, apellido_p, apellido_m, edad, no_empleado, salario)
        lista.append(empleado)

    if opcion == 2:
        area = input("Área del empleado: ")
        disenador = Disenador(nombre, apellido_p, apellido_m, edad, no_empleado, salario,area)
        lista.append(disenador)
