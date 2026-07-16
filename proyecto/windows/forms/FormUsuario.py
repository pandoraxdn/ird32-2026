from PySide6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit, QDateEdit, QComboBox,
    QDialogButtonBox, QMessageBox
)
from db.crud_usuario import crear_usuario, actualizar_usuario

class FormUsuario(QDialog):
    def __init__(self, usuario=None, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setWindowTitle("Usuario" if usuario is None else "Editar Usuario")
        self.setup_ui()
        if usuario:
            self.cargar_datos(usuario)

    def setup_ui(self):
        layout = QFormLayout(self)

        self.nombre = QLineEdit()
        self.email = QLineEdit()
        self.telefono = QLineEdit()
        self.direccion = QLineEdit()
        self.fecha_nac = QDateEdit()
        self.fecha_nac.setCalendarPopup(True)
        self.fecha_nac.setDisplayFormat("yyyy-MM-dd")
        self.activo = QComboBox()
        self.activo.addItems(["Activo", "Inactivo"])

        layout.addRow("Nombre:", self.nombre)
        layout.addRow("Email:", self.email)
        layout.addRow("Teléfono:", self.telefono)
        layout.addRow("Dirección:", self.direccion)
        layout.addRow("Fecha nacimiento:", self.fecha_nac)
        layout.addRow("Estado:", self.activo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.aceptar)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def cargar_datos(self, usuario):
        self.nombre.setText(usuario.nombre)
        self.email.setText(usuario.email)
        self.telefono.setText(usuario.telefono or "")
        self.direccion.setText(usuario.direccion or "")
        if usuario.fecha_nacimiento:
            self.fecha_nac.setDate(usuario.fecha_nacimiento)
        self.activo.setCurrentIndex(0 if usuario.activo else 1)

    def aceptar(self):
        datos = {
            "nombre": self.nombre.text(),
            "email": self.email.text(),
            "telefono": self.telefono.text() or None,
            "direccion": self.direccion.text() or None,
            "fecha_nacimiento": self.fecha_nac.date().toString("yyyy-MM-dd"),
            "activo": self.activo.currentIndex() == 0
        }
        try:
            if self.usuario is None:
                crear_usuario(**datos)
            else:
                actualizar_usuario(self.usuario.id_usuario, **datos)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
