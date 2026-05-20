from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido_p, apellido_m, edad, no_empleado, salario) -> None:
        super().__init__(nombre, apellido_p, apellido_m, edad)
        self._no_empleado = no_empleado
        self._salario = salario

    def __str__(self) -> str:
        return f"""
        Nombre: {self.nombre}
        Apellido Paterno: {self.apellido_p}
        Apellido Materno: {self.apellido_m}
        Edad: {self.edad}
        Número Empleado: {self.no_empleado}
        Salario: {self.salario}
    """

    @property
    def no_empleado(self):
        return self._no_empleado

    @property
    def salario(self):
        return self._salario

    @no_empleado.setter
    def no_empleado(self,no_empleado):
        self._no_empleado = no_empleado

    @salario.setter
    def salario(self,salario):
        self._salario = salario  

if __name__ == "__main__":
    empleado1 = Empleado("Sara","Lopez","Suarez",23,114,2500)
    print(empleado1)

    empleado1.no_empleado = 115
    empleado1.salario = 1900
    print(empleado1)
