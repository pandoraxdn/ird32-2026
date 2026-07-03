from PySide6.QtWidgets import(
    QWidget as Ventana,
    QLabel as Texto,
    QLineEdit as Entrada,
    QTextEdit as Entrada2,
    QPushButton as Boton,
    QVBoxLayout as ContenedorV,
    QComboBox as Combo,
    QDateEdit as Fecha,
    QSpinBox as Spin,
)

class FormWindow(Ventana):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.crear_interfaz()

    def configurar_ventana(self):
        self.setWindowTitle("Formulario")
        self.resize(800,700)

    def crear_interfaz(self):
        contenedor_principal = ContenedorV();
        contenedor_principal.setSpacing(18)
        titulo = Texto("Formulario")
        titulo.setObjectName("titulo")
        correo = Entrada()
        correo.setPlaceholderText("Ingresa el correo del usuario")
        puesto = Combo()
        puesto.addItems([
            "Administración",
            "Sistemas",
            "Marketig",
            "Producción",
            "Inventario"
        ])
        edad = Spin()
        edad.setRange(18,70)
        fecha = Fecha()

        responsabilidades = Entrada2()
        responsabilidades.setPlaceholderText("Ingrese las responsabilidades")

        boton = Boton("Guardar")

        contenedor_principal.addWidget(titulo)
        contenedor_principal.addWidget(correo)
        contenedor_principal.addWidget(puesto)
        contenedor_principal.addWidget(edad)
        contenedor_principal.addWidget(fecha)
        contenedor_principal.addWidget(responsabilidades)
        contenedor_principal.addWidget(boton)

        self.setLayout(contenedor_principal)




