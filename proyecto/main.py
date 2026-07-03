import sys
from PySide6.QtWidgets import QApplication as App
#from windows.LoginWindow import LoginWindow
from windows.FormWindow import FormWindow
from db.database import Engine, Base
from db.models import Usuario, Producto, Pedido, DetallePedido

Base.metadata.create_all(bind=Engine)

def main():
    app = App()
    ventana = FormWindow()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
