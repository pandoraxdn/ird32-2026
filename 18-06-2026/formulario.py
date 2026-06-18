import sys
from PySide6.QtWidgets import QApplication as App
from PySide6.QtWidgets import QWidget as Ventana
from PySide6.QtWidgets import QPushButton as Boton
from PySide6.QtWidgets import QTextEdit as Entrada
from PySide6.QtWidgets import QFormLayout as Contendor

app = App()
ventana = Ventana()
ventana.setWindowTitle("Registro de datos")
ventana.resize(600,300)

formulario = Contendor()
formulario.addRow("Nombre: ",Entrada())
formulario.addRow("E-mail: ",Entrada())
formulario.addRow("Edad: ",Entrada())
formulario.addRow("Enviar datos: ",Boton("Enviar"))

ventana.setLayout(formulario)
ventana.show()
sys.exit(app.exec())
