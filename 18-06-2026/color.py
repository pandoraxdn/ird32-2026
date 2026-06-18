import sys
from PySide6.QtWidgets import QApplication as App
from PySide6.QtWidgets import QWidget as Ventana
from PySide6.QtWidgets import QPushButton as Boton
from PySide6.QtWidgets import QColorDialog as Color
from PySide6.QtWidgets import QVBoxLayout as Contenedor
from PySide6.QtGui import QPalette

def elegir_color():
    color = Color.getColor()
    if color.isValid():
        palette = ventana.palette()
        palette.setColor(QPalette.Window,color)
        ventana.setPalette(palette)


app = App(sys.argv)
ventana = Ventana()
ventana.resize(400,300)
contenedor = Contenedor()
boton = Boton("Cambia el color...")
boton.clicked.connect(elegir_color)
contenedor.addWidget(boton)
ventana.setLayout(contenedor)
ventana.show()
sys.exit(app.exec())
