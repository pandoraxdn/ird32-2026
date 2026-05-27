cantidad = int(input())

lista = []

if cantidad >= 1 and cantidad <= 10**5:
    
    for element in range(cantidad):
        datos = [ value for value in input().split()]
        
        if int(datos[2]) <= 1 or int(datos[2]) >= 10**6:
            continue
        if int(datos[3]) <= 1 or int(datos[3]) >= 10**4:
            continue
        
        lista.append({
            "nombre": datos[0],
            "categoria": datos[1],
            "precio": float(datos[2]),
            "cantidad": float(datos[3]),
        })
        
total = 0
    
for element in lista:
    total += element["precio"] * element["cantidad"]

print(f"\nTOTAL_GENERAL: {total}")

producto = ""

for element in lista:
    if producto == "":
        producto = element["precio"]
    else:
        if producto < element["precio"]:
            producto = element["precio"]

nombre = "" 
for element in lista:
    if element["precio"] == producto:
        nombre = element["nombre"]

print(f"PRODUCTO_TOP: {nombre}")
print(f"PROMEDIO_VENTA:{total/len(lista)}")
print(f"TOTAL_PRODUCTOS:{len(lista)}")
