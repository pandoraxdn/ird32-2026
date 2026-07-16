from pathlib import Path
from PySide6.QtWidgets import (
    QWidget as Ventana,
    QLabel as Texto,
    QPushButton as Boton,
    QLineEdit as Entrada,
    QVBoxLayout as ContenedorV,
    QFrame as Frame,
    QCheckBox as Check,
    QMessageBox
)
from db.crud_usuario import obtener_usuario_por_email

class LoginWindow(Ventana):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.crear_interfaz()
        self.cargar_estilos()
        self.conectar_signales()

    def configurar_ventana(self):
        self.setWindowTitle("Sistema Empresarial")
        self.resize(600, 400)

    def crear_interfaz(self):
        contenedor_principal = ContenedorV()
        contenedor_principal.setContentsMargins(20, 20, 20, 20)
        contenedor_principal.setSpacing(25)

        tarjeta = Frame()
        tarjeta.setObjectName("tarjeta")

        contenedor_tarjeta = ContenedorV()
        contenedor_tarjeta.setContentsMargins(40, 40, 40, 40)
        contenedor_tarjeta.setSpacing(20)

        logo = Texto("🖥️")
        logo.setObjectName("logo")
        subtitulo = Texto("Ingrese Credenciales")
        subtitulo.setObjectName("subtitulo")

        self.correo = Entrada()
        self.correo.setPlaceholderText("Correo Electrónico")
        self.correo.setObjectName("correo")

        self.password = Entrada()
        self.password.setPlaceholderText("Contraseña")
        self.password.setObjectName("password")
        self.password.setEchoMode(Entrada.Password)

        self.recordar = Check("Recordar contraseña")
        self.recordar.setObjectName("recordar")

        self.boton = Boton("Iniciar Sesión")
        self.boton.setObjectName("boton")

        contenedor_tarjeta.addWidget(logo)
        contenedor_tarjeta.addWidget(subtitulo)
        contenedor_tarjeta.addWidget(self.correo)
        contenedor_tarjeta.addWidget(self.password)
        contenedor_tarjeta.addWidget(self.recordar)
        contenedor_tarjeta.addWidget(self.boton)

        tarjeta.setLayout(contenedor_tarjeta)
        contenedor_principal.addWidget(tarjeta)
        self.setLayout(contenedor_principal)

    def cargar_estilos(self):
        ruta_estilos = Path(__file__).parent.parent / "styles" / "login.qss"
        if ruta_estilos.exists():
            with open(ruta_estilos, "r", encoding="utf-8") as archivo:
                self.setStyleSheet(archivo.read())
        else:
            print("Archivo de estilos no encontrado")

    def conectar_signales(self):
        self.boton.clicked.connect(self.autenticar)

    def autenticar(self):
        email = self.correo.text().strip()
        password = self.password.text().strip()  # En realidad no se usa, falta hashear
        if not email or not password:
            QMessageBox.warning(self, "Campos vacíos", "Por favor ingrese correo y contraseña.")
            return

        # Buscar usuario por email
        usuario = obtener_usuario_por_email(email)
        if usuario and usuario.activo:
            # Aquí deberías comparar la contraseña hasheada (aún no implementada)
            QMessageBox.information(self, "Éxito", f"Bienvenido {usuario.nombre}")
            # Abrir ventana principal (AdminWindow)
            self.abrir_admin()
        else:
            QMessageBox.critical(self, "Error", "Credenciales incorrectas o usuario inactivo")

    def abrir_admin(self):
        from windows.AdminWindow import AdminWindow  # import local para evitar ciclo
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.close()  # cierra login
