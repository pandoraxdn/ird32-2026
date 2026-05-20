# Un diccionario en arreglo o conjunto de elementos
# la diferencia radica en su asingación por medio
# de clave:valor
persona = {
    "nombre": "Ricardo",
    "apellido_paterno": "Lopez",
    "edad": 28,
}

persona["nombre"] = "Sofia"
persona["estatura"] = 1.60

print(persona["estatura"])


for clave, valor in persona.items():
    print(f"Clave: {clave} Valor: {valor}")


