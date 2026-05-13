condicion1, condicion2 = True, True

# AND
print( condicion1 and condicion2 and True )

# OR
print( condicion1 or condicion2 or False )

# Negación/not
print(not False)

edad = 37

if edad >= 30:
    print("Ya estas grande")
elif edad == 18:
    print("Tienes 18 años")
elif edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


print(["Eres menor de edad","Eres mayor de edad"][edad >= 18])






