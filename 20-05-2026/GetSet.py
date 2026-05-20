
class Auto:

    def __init__(self,marca, modelo, color) -> None:
        self._marca = marca
        self._modelo = modelo
        self._color = color

    # Get me permite acceder a los atributos
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def color(self):
        return self._color

    # Setters me permite asingar valores a los atributos
    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo

    @color.setter
    def color(self,color):
        self._color = color

auto1 = Auto("Mercedes","BMW","azul")
print(auto1.marca)
auto1.marca = "Ford"
print(auto1.marca)



