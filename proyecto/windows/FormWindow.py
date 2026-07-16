from PySide6.QtWidgets import (
    QWidget as Ventana,
    QLabel as Texto,
    QLineEdit as Entrada,
    QTextEdit as Entrada2,
    QPushButton as Boton,
    QVBoxLayout as ContenedorV,
    QComboBox as Combo,
    QDateEdit as Fecha,
    QSpinBox as Spin,
    QMessageBox
)
from PySide6.QtCore import QDate

class FormWindow(Ventana):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.crear_interfaz()
        self.conectar_signales()

    def configurar_ventana(self):
        self.setWindowTitle("Formulario")
        self.resize(800, 700)

    def crear_interfaz(self):
        contenedor_principal = ContenedorV()
        contenedor_principal.setSpacing(18)

        titulo = Texto("Formulario")
        titulo.setObjectName("titulo")

        self.correo = Entrada()
        self.correo.setPlaceholderText("Ingresa el correo del usuario")
        self.correo.setObjectName("correo")

        self.puesto = Combo()
        self.puesto.addItems([
            "Administración",
            "Sistemas",
            "Marketing",
            "Producción",
            "Inventario"
        ])
        self.puesto.setObjectName("puesto")

        self.edad = Spin()
        self.edad.setRange(18, 70)
        self.edad.setObjectName("edad")

        self.fecha = Fecha()
        self.fecha.setDate(QDate.currentDate())
        self.fecha.setObjectName("fecha")

        self.responsabilidades = Entrada2()
        self.responsabilidades.setPlaceholderText("Ingrese las responsabilidades")
        self.responsabilidades.setObjectName("responsabilidades")

        self.boton = Boton("Guardar")
        self.boton.setObjectName("boton_guardar")

        contenedor_principal.addWidget(titulo)
        contenedor_principal.addWidget(self.correo)
        contenedor_principal.addWidget(self.puesto)
        contenedor_principal.addWidget(self.edad)
        contenedor_principal.addWidget(self.fecha)
        contenedor_principal.addWidget(self.responsabilidades)
        contenedor_principal.addWidget(self.boton)

        self.setLayout(contenedor_principal)

    def conectar_signales(self):
        self.boton.clicked.connect(self.guardar)

    def guardar(self):
        # Aquí puedes procesar los datos
        datos = {
            "correo": self.correo.text(),
            "puesto": self.puesto.currentText(),
            "edad": self.edad.value(),
            "fecha": self.fecha.date().toString("yyyy-MM-dd"),
            "responsabilidades": self.responsabilidades.toPlainText()
        }
        # Validar
        if not datos["correo"]:
            QMessageBox.warning(self, "Error", "El correo es obligatorio")
            return
        # Aquí llamarías a un CRUD para guardar
        QMessageBox.information(self, "Éxito", f"Datos guardados:\n{datos}")
