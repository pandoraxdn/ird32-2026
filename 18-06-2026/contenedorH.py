import sys
from PySide6.QtWidgets import QApplication as App
from PySide6.QtWidgets import QWidget as Ventana
from PySide6.QtWidgets import QPushButton as Boton
# QVBoxLayout Contendor vertical
# QHBoxLayout Contendor horizontal
from PySide6.QtWidgets import QHBoxLayout as Contendor

app = App()
ventana = Ventana()
ventana.setWindowTitle("Registro de datos")
ventana.resize(1000,700)

contenedor = Contendor()
boton1 = Boton("Boton 1")
boton2 = Boton("Boton 2")
boton3 = Boton("Boton 3")

contenedor.addWidget(boton1)
contenedor.addWidget(boton2)
contenedor.addWidget(boton3)

ventana.setLayout(contenedor)
ventana.show()
sys.exit(app.exec())
