from Empleado import Empleado

class Disenador(Empleado):
    def __init__(self, nombre, apellido_p, apellido_m, edad, no_empleado, salario, area) -> None:
        super().__init__(nombre, apellido_p, apellido_m, edad, no_empleado, salario)
        self._area = area

    def __str__(self) -> str:
        return f"""
        Nombre: {self.nombre}
        Apellido Paterno: {self.apellido_p}
        Apellido Materno: {self.apellido_m}
        Edad: {self.edad}
        Número Empleado: {self.no_empleado}
        Salario: {self.salario}
        Área: {self.area}
    """

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self,area):
        self._area = area

if __name__ == "__main__":
    disenador1 = Disenador("Lupita","Ruiz","Perez",23,116,3000,"Marketing")
    print(disenador1)

    disenador1.area = "Sistemas"
    print(disenador1)
