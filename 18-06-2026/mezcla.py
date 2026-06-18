import sys
from PySide6.QtWidgets import QApplication as App
from PySide6.QtWidgets import QWidget as Ventana
from PySide6.QtWidgets import QPushButton as Boton
from PySide6.QtWidgets import QVBoxLayout as ContendorV
from PySide6.QtWidgets import QHBoxLayout as ContendorH

app = App()
ventana = Ventana()
ventana.setWindowTitle("Registro de datos")
ventana.resize(600,300)
contenedor_principal = ContendorV()

contenedor_sub = ContendorH()
contenedor_sub.addWidget(Boton("1"))
contenedor_sub.addWidget(Boton("2"))
contenedor_sub.addWidget(Boton("3"))
contenedor_sub.addWidget(Boton("4"))

info = ContendorH()
info.addWidget(Boton("5"))
info.addWidget(Boton("6"))
info.addWidget(Boton("7"))
info.addWidget(Boton("8"))

contenedor_principal.addLayout(contenedor_sub)
contenedor_principal.addLayout(info)

ventana.setLayout(contenedor_principal)
ventana.show()
sys.exit(app.exec())
