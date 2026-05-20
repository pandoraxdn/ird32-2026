class Persona:
    def __init__(self,nombre, apellido_p, apellido_m, edad) -> None:
        self._nombre = nombre
        self._apellido_p = apellido_p
        self._apellido_m = apellido_m
        self._edad = edad

    def __str__(self) -> str:
        return f"""
        Nombre: {self.nombre}
        Apellido Paterno: {self.apellido_p}
        Apellido Materno: {self.apellido_m}
        Edad: {self.edad}
    """

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido_p(self):
        return self._apellido_p

    @property
    def apellido_m(self):
        return self._apellido_m

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido_p.setter
    def apellido_p(self, apellido_p):
        self._apellido_p = apellido_p

    @apellido_m.setter
    def apellido_m(self, apellido_m):
        self._apellido_m = apellido_m

    @edad.setter
    def edad(self, edad):
        self._edad = edad

if __name__ == "__main__":
    # Ejecutar cuando se ejecute:
    # python Persona.py
    persona1 = Persona("Nadia","Olvera","Lopez",23)
    print(persona1)

    persona1.nombre = "Daniela"

    persona1.apellido_p = "Ruiz"

    persona1.apellido_m = "Suarez"

    persona1.edad = 25

    print(persona1)
