import sys
from PySide6.QtWidgets import QApplication as App
from PySide6.QtWidgets import QWidget as Ventana
from PySide6.QtWidgets import QPushButton as Boton
from PySide6.QtWidgets import QMessageBox as Mensaje
from PySide6.QtWidgets import QVBoxLayout as Contendor

def mensaje():
    respuesta = Mensaje.question(
                None,
                "Salir", # Title
                "¿Estás seguro?", # Message
                Mensaje.Yes | Mensaje.No
            )
    if respuesta == Mensaje.Yes:
        print("Saliendo")
        App.quit()

app = App(sys.argv)
ventana = Ventana()
ventana.resize(400,300)
contenedor = Contendor()

boton = Boton("Salir")
boton.clicked.connect(mensaje)

contenedor.addWidget(boton)
ventana.setLayout(contenedor)
ventana.show()
sys.exit(app.exec())
