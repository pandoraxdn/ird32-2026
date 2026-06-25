import sys
from PySide6.QtWidgets import QApplication as App
#from windows.LoginWindow import LoginWindow
from windows.FormWindow import FormWindow

def main():
    app = App()
    ventana = FormWindow()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
