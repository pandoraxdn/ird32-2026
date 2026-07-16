from PySide6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit, QSpinBox, QTextEdit,
    QDialogButtonBox, QMessageBox
)
from db.crud_productos import crear_producto, actualizar_producto

class FormProducto(QDialog):
    def __init__(self, producto=None, parent=None):
        super().__init__(parent)
        self.producto = producto
        self.setWindowTitle("Producto" if producto is None else "Editar Producto")
        self.setup_ui()
        if producto:
            self.cargar_datos(producto)

    def setup_ui(self):
        layout = QFormLayout(self)

        self.nombre = QLineEdit()
        self.precio = QLineEdit()
        self.stock = QSpinBox()
        self.stock.setRange(0, 999999)
        self.descripcion = QTextEdit()
        self.categoria = QLineEdit()
        self.proveedor = QLineEdit()
        self.peso = QLineEdit()
        self.dimensiones = QLineEdit()

        layout.addRow("Nombre:", self.nombre)
        layout.addRow("Precio:", self.precio)
        layout.addRow("Stock:", self.stock)
        layout.addRow("Descripción:", self.descripcion)
        layout.addRow("Categoría:", self.categoria)
        layout.addRow("Proveedor:", self.proveedor)
        layout.addRow("Peso kg:", self.peso)
        layout.addRow("Dimensiones:", self.dimensiones)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.aceptar)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def cargar_datos(self, producto):
        self.nombre.setText(producto.nombre)
        self.precio.setText(str(producto.precio))
        self.stock.setValue(producto.stock)
        self.descripcion.setText(producto.descripcion or "")
        self.categoria.setText(producto.categoria or "")
        self.proveedor.setText(producto.proveedor or "")
        self.peso.setText(str(producto.peso_kg) if producto.peso_kg else "")
        self.dimensiones.setText(producto.dimensiones or "")

    def aceptar(self):
        try:
            precio_val = float(self.precio.text())
            peso_val = float(self.peso.text()) if self.peso.text() else None
        except ValueError:
            QMessageBox.warning(self, "Error", "Precio y peso deben ser números.")
            return
        datos = {
            "nombre": self.nombre.text(),
            "precio": precio_val,
            "stock": self.stock.value(),
            "descripcion": self.descripcion.toPlainText() or None,
            "categoria": self.categoria.text() or None,
            "proveedor": self.proveedor.text() or None,
            "peso_kg": peso_val,
            "dimensiones": self.dimensiones.text() or None
        }
        try:
            if self.producto is None:
                crear_producto(**datos)
            else:
                actualizar_producto(self.producto.id_producto, **datos)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
