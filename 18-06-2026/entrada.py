import sys
from PySide6.QtWidgets import QApplication as App
from PySide6.QtWidgets import QWidget as Ventana
from PySide6.QtWidgets import QLabel as Texto
from PySide6.QtWidgets import QPushButton as Boton
from PySide6.QtWidgets import QTextEdit as Entrada
from PySide6.QtWidgets import QVBoxLayout as Contendor

app = App()
ventana = Ventana()
ventana.setWindowTitle("Registro de datos")
ventana.resize(1000,700)

contenedor = Contendor()
texto = Texto("Texto ingresado: ")
entrada = Entrada()
boton = Boton("Enviar texto")

def enviar():
    texto.setText(f"Texto ingresado {entrada.toPlainText()}")

boton.clicked.connect(enviar)

contenedor.addWidget(texto)
contenedor.addWidget(entrada)
contenedor.addWidget(boton)

ventana.setLayout(contenedor)
ventana.show()
sys.exit(app.exec())












