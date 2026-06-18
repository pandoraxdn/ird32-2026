import sys
from PySide6.QtWidgets import QApplication as App
from PySide6.QtWidgets import QWidget as Ventana
from PySide6.QtWidgets import QPushButton as Boton
from PySide6.QtWidgets import QGridLayout as Contendor

app = App()
ventana = Ventana()
ventana.setWindowTitle("Registro de datos")
ventana.resize(600,300)

grid = Contendor()

grid.addWidget(Boton("(0,0)"),0,0)
grid.addWidget(Boton("(0,1)"),0,1)
grid.addWidget(Boton("(1,0)"),1,0)
grid.addWidget(Boton("(1,1)"),1,1)

ventana.setLayout(grid)
ventana.show()
sys.exit(app.exec())
