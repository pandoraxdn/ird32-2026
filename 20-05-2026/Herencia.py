class Animal:
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    def comer(self):
        print("Como muchas veces a día")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

class Perro(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def hacer_ruido(self):
        print("Ladrar")


animal1 = Animal("Delfin")
animal1.comer()

animal2 = Perro("Chihuahua")
animal2.hacer_ruido()
animal2.comer()




