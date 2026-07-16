from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget,
    QTableWidgetItem, QHeaderView, QMessageBox, QStackedWidget,
    QFrame, QLabel, QSizePolicy, QDialog
)
from PySide6.QtCore import Qt
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.crud_productos import (
    obtener_producto_por_id, obtener_todos_productos,
    eliminar_producto_fisico as eliminar_producto
)
from db.crud_usuario import (
    obtener_usuario_por_id, obtener_todos_usuarios,
    eliminar_usuario_fisico
)
from db.crud_pedidos import (
    obtener_pedido_por_id, obtener_todos_pedidos,
    eliminar_pedido_fisico
)

from windows.forms.FormUsuario import FormUsuario
from windows.forms.FormProducto import FormProducto
from windows.forms.FormPedido import FormPedido

class AdminWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Panel de Administración")
        self.resize(1200, 700)
        self.current_table = None
        self.init_ui()
        self.cargar_estilos()
        self.cargar_usuarios()

    def init_ui(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.content_stack = QStackedWidget()
        self.content_stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.table_widget = QTableWidget()
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_widget.setSelectionMode(QTableWidget.SingleSelection)

        button_layout = QHBoxLayout()
        self.btn_add = QPushButton("Agregar")
        self.btn_edit = QPushButton("Editar")
        self.btn_delete = QPushButton("Eliminar")
        self.btn_refresh = QPushButton("Actualizar")
        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_edit)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_refresh)
        button_layout.addStretch()

        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.table_widget)
        content_layout.addLayout(button_layout)
        content_widget.setLayout(content_layout)

        self.content_stack.addWidget(content_widget)

        menu_frame = QFrame()
        menu_frame.setObjectName("menuFrame")
        menu_frame.setFixedWidth(250)

        menu_layout = QVBoxLayout()
        menu_layout.setContentsMargins(20, 30, 20, 30)
        menu_layout.setSpacing(15)

        title = QLabel("Módulos")
        title.setObjectName("menuTitle")
        title.setAlignment(Qt.AlignCenter)
        menu_layout.addWidget(title)
        menu_layout.addSpacing(20)

        self.btn_usuarios = QPushButton("Usuarios")
        self.btn_usuarios.setObjectName("menuButton")
        self.btn_usuarios.clicked.connect(self.cargar_usuarios)

        self.btn_productos = QPushButton("Productos")
        self.btn_productos.setObjectName("menuButton")
        self.btn_productos.clicked.connect(self.cargar_productos)

        self.btn_pedidos = QPushButton("Pedidos")
        self.btn_pedidos.setObjectName("menuButton")
        self.btn_pedidos.clicked.connect(self.cargar_pedidos)

        self.btn_logout = QPushButton("Cerrar sesión")
        self.btn_logout.setObjectName("menuButton")
        self.btn_logout.clicked.connect(self.close)

        menu_layout.addWidget(self.btn_usuarios)
        menu_layout.addWidget(self.btn_productos)
        menu_layout.addWidget(self.btn_pedidos)
        menu_layout.addStretch()
        menu_layout.addWidget(self.btn_logout)

        menu_frame.setLayout(menu_layout)

        main_layout.addWidget(menu_frame, 0)
        main_layout.addWidget(self.content_stack, 1)

        self.setLayout(main_layout)

        self.btn_add.clicked.connect(self.agregar_registro)
        self.btn_edit.clicked.connect(self.editar_registro)
        self.btn_delete.clicked.connect(self.eliminar_registro)
        self.btn_refresh.clicked.connect(self.refrescar_tabla)

    def cargar_estilos(self):
        carpeta_actual = os.path.dirname(os.path.abspath(__file__))
        file_qss = os.path.join(carpeta_actual, '..', 'styles', 'admin.qss')
        if os.path.exists(file_qss):
            with open(file_qss, "r", encoding="utf-8") as archivo:
                self.setStyleSheet(archivo.read())

    def cargar_usuarios(self):
        usuarios = obtener_todos_usuarios() or []
        self.mostrar_tabla_usuarios(usuarios)
        self.content_stack.setCurrentIndex(0)
        self.current_table = "usuarios"

    def mostrar_tabla_usuarios(self, datos):
        self.table_widget.clear()
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Email", "Teléfono", "Dirección", "Activo"]
        )
        self.table_widget.setRowCount(len(datos))
        for i, row in enumerate(datos):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(row.id_usuario)))
            self.table_widget.setItem(i, 1, QTableWidgetItem(row.nombre))
            self.table_widget.setItem(i, 2, QTableWidgetItem(row.email))
            self.table_widget.setItem(i, 3, QTableWidgetItem(row.telefono or ""))
            self.table_widget.setItem(i, 4, QTableWidgetItem(row.direccion or ""))
            self.table_widget.setItem(i, 5, QTableWidgetItem("Sí" if row.activo else "No"))

    def cargar_productos(self):
        productos = obtener_todos_productos() or []
        self.mostrar_tabla_productos(productos)
        self.content_stack.setCurrentIndex(0)
        self.current_table = "productos"

    def mostrar_tabla_productos(self, datos):
        self.table_widget.clear()
        self.table_widget.setColumnCount(7)
        self.table_widget.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Precio", "Stock", "Categoría", "Proveedor", "Peso kg"]
        )
        self.table_widget.setRowCount(len(datos))
        for i, row in enumerate(datos):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(row.id_producto)))
            self.table_widget.setItem(i, 1, QTableWidgetItem(row.nombre))
            self.table_widget.setItem(i, 2, QTableWidgetItem(str(row.precio)))
            self.table_widget.setItem(i, 3, QTableWidgetItem(str(row.stock)))
            self.table_widget.setItem(i, 4, QTableWidgetItem(row.categoria or ""))
            self.table_widget.setItem(i, 5, QTableWidgetItem(row.proveedor or ""))
            self.table_widget.setItem(i, 6, QTableWidgetItem(str(row.peso_kg) if row.peso_kg else ""))

    def cargar_pedidos(self):
        pedidos = obtener_todos_pedidos() or []
        self.mostrar_tabla_pedidos(pedidos)
        self.content_stack.setCurrentIndex(0)
        self.current_table = "pedidos"

    def mostrar_tabla_pedidos(self, datos):
        self.table_widget.clear()
        self.table_widget.setColumnCount(7)
        self.table_widget.setHorizontalHeaderLabels(
            ["ID", "Usuario ID", "Estado", "Fecha", "Método Pago", "Descuento", "Comentarios"]
        )
        self.table_widget.setRowCount(len(datos))
        for i, row in enumerate(datos):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(row.id_pedido)))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(row.usuario_id)))
            self.table_widget.setItem(i, 2, QTableWidgetItem(row.estado))
            self.table_widget.setItem(i, 3, QTableWidgetItem(str(row.fecha_pedido)))
            self.table_widget.setItem(i, 4, QTableWidgetItem(row.metodo_pago or ""))
            self.table_widget.setItem(i, 5, QTableWidgetItem(str(row.descuento_total)))
            self.table_widget.setItem(i, 6, QTableWidgetItem(row.comentarios or ""))

    def refrescar_tabla(self):
        if self.current_table == "usuarios":
            self.cargar_usuarios()
        elif self.current_table == "productos":
            self.cargar_productos()
        elif self.current_table == "pedidos":
            self.cargar_pedidos()

    def agregar_registro(self):
        if self.current_table == "usuarios":
            self.abrir_formulario_usuario(None)
        elif self.current_table == "productos":
            self.abrir_formulario_producto(None)
        elif self.current_table == "pedidos":
            self.abrir_formulario_pedido(None)

    def editar_registro(self):
        selected = self.table_widget.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Seleccionar", "Seleccione un registro para editar.")
            return
        id_item = self.table_widget.item(selected, 0)
        if not id_item:
            return
        id_registro = int(id_item.text())
        if self.current_table == "usuarios":
            usuario = obtener_usuario_por_id(id_registro)
            if usuario:
                self.abrir_formulario_usuario(usuario)
        elif self.current_table == "productos":
            producto = obtener_producto_por_id(id_registro)
            if producto:
                self.abrir_formulario_producto(producto)
        elif self.current_table == "pedidos":
            pedido = obtener_pedido_por_id(id_registro)
            if pedido:
                self.abrir_formulario_pedido(pedido)

    def eliminar_registro(self):
        selected = self.table_widget.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Seleccionar", "Seleccione un registro para eliminar.")
            return
        id_item = self.table_widget.item(selected, 0)
        if not id_item:
            return
        id_registro = int(id_item.text())
        confirm = QMessageBox.question(
            self, "Confirmar", f"¿Eliminar registro {id_registro}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            try:
                if self.current_table == "usuarios":
                    eliminar_usuario_fisico(id_registro)
                elif self.current_table == "productos":
                    eliminar_producto(id_registro)
                elif self.current_table == "pedidos":
                    eliminar_pedido_fisico(id_registro)
                self.refrescar_tabla()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar: {e}")

    def abrir_formulario_usuario(self, usuario):
        form = FormUsuario(usuario, self)
        if form.exec() == QDialog.Accepted:
            self.refrescar_tabla()

    def abrir_formulario_producto(self, producto):
        form = FormProducto(producto, self)
        if form.exec() == QDialog.Accepted:
            self.refrescar_tabla()

    def abrir_formulario_pedido(self, pedido):
        form = FormPedido(pedido, self)
        if form.exec() == QDialog.Accepted:
            self.refrescar_tabla()
