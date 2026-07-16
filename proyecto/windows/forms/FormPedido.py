from PySide6.QtWidgets import (
    QDialog, QFormLayout, QVBoxLayout, QHBoxLayout, QLineEdit,
    QDateEdit, QComboBox, QTextEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QHeaderView, QMessageBox, QDialogButtonBox,
    QSpinBox, QDoubleSpinBox
)
from PySide6.QtCore import Qt, QDate
from db.crud_usuario import obtener_todos_usuarios
from db.crud_productos import obtener_todos_productos
from db.crud_pedidos import crear_pedido, actualizar_pedido
from db.crud_detalle_pedido import (
    crear_detalle, eliminar_detalles_por_pedido,
    obtener_detalles_por_pedido, actualizar_detalle
)

class FormPedido(QDialog):
    def __init__(self, pedido=None, parent=None):
        super().__init__(parent)
        self.pedido = pedido
        self.detalles_actuales = []
        self.detalles_existentes = []
        self.setWindowTitle("Pedido" if pedido is None else "Editar Pedido")
        self.resize(800, 600)
        self.setup_ui()
        self.cargar_combos()
        if pedido:
            self.cargar_datos_pedido(pedido)
            self.cargar_detalles_existentes(pedido.id_pedido)

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Formulario principal
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)

        self.usuario_combo = QComboBox()
        self.estado_combo = QComboBox()
        self.estado_combo.addItems(["PENDIENTE", "PROCESANDO", "ENVIADO", "ENTREGADO", "CANCELADO"])
        self.metodo_pago = QLineEdit()
        self.metodo_pago.setPlaceholderText("Ej: Tarjeta, Efectivo, Transferencia")
        self.fecha_entrega = QDateEdit()
        self.fecha_entrega.setCalendarPopup(True)
        self.fecha_entrega.setDisplayFormat("yyyy-MM-dd")
        self.fecha_entrega.setDate(QDate.currentDate().addDays(7))
        self.comentarios = QTextEdit()
        self.comentarios.setMaximumHeight(80)
        self.descuento_total = QLineEdit()
        self.descuento_total.setPlaceholderText("0.00")

        form_layout.addRow("Usuario:", self.usuario_combo)
        form_layout.addRow("Estado:", self.estado_combo)
        form_layout.addRow("Método pago:", self.metodo_pago)
        form_layout.addRow("Fecha entrega:", self.fecha_entrega)
        form_layout.addRow("Comentarios:", self.comentarios)
        form_layout.addRow("Descuento total:", self.descuento_total)

        layout.addWidget(form_widget)

        # Tabla de detalles
        self.table_detalles = QTableWidget()
        self.table_detalles.setColumnCount(6)
        self.table_detalles.setHorizontalHeaderLabels(
            ["Producto", "Cantidad", "Precio Unit.", "Descuento", "Subtotal", "Acciones"]
        )
        self.table_detalles.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_detalles.setSelectionBehavior(QTableWidget.SelectRows)
        self.table_detalles.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.table_detalles)

        # Botones para añadir/eliminar detalles
        btn_layout = QHBoxLayout()
        self.btn_agregar_detalle = QPushButton("Agregar Producto")
        self.btn_eliminar_detalle = QPushButton("Eliminar Producto Seleccionado")
        btn_layout.addWidget(self.btn_agregar_detalle)
        btn_layout.addWidget(self.btn_eliminar_detalle)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Botones Aceptar/Cancelar
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.aceptar)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        # Conectar señales
        self.btn_agregar_detalle.clicked.connect(self.agregar_detalle)
        self.btn_eliminar_detalle.clicked.connect(self.eliminar_detalle_seleccionado)

        # Inicializar lista de detalles vacía
        self.detalles_actuales = []

    def cargar_combos(self):
        # Cargar usuarios
        usuarios = obtener_todos_usuarios() or []
        self.usuario_combo.clear()
        for u in usuarios:
            self.usuario_combo.addItem(f"{u.nombre} (ID: {u.id_usuario})", u.id_usuario)
        if self.usuario_combo.count() == 0:
            self.usuario_combo.addItem("No hay usuarios", -1)

    def cargar_datos_pedido(self, pedido):
        # Seleccionar usuario en combo
        idx = self.usuario_combo.findData(pedido.usuario_id)
        if idx >= 0:
            self.usuario_combo.setCurrentIndex(idx)
        self.estado_combo.setCurrentText(pedido.estado)
        self.metodo_pago.setText(pedido.metodo_pago or "")
        if pedido.fecha_entrega:
            self.fecha_entrega.setDate(pedido.fecha_entrega)
        self.comentarios.setText(pedido.comentarios or "")
        self.descuento_total.setText(str(pedido.descuento_total))

    def cargar_detalles_existentes(self, pedido_id):
        detalles = obtener_detalles_por_pedido(pedido_id)
        self.detalles_existentes = detalles
        self.detalles_actuales = []
        for det in detalles:
            # Guardamos los datos del detalle en un dict para edición posterior
            self.detalles_actuales.append({
                "id_detalle": det.id_detalle_producto,
                "producto_id": det.producto_id,
                "producto_nombre": det.producto.nombre if det.producto else "Desconocido",
                "cantidad": det.cantidad,
                "precio_unitario": det.precio_unitario,
                "descuento": det.descuento_aplicado,
                "subtotal": det.subtotal
            })
        self.refrescar_tabla_detalles()

    def refrescar_tabla_detalles(self):
        self.table_detalles.setRowCount(len(self.detalles_actuales))
        for i, det in enumerate(self.detalles_actuales):
            self.table_detalles.setItem(i, 0, QTableWidgetItem(det["producto_nombre"]))
            self.table_detalles.setItem(i, 1, QTableWidgetItem(str(det["cantidad"])))
            self.table_detalles.setItem(i, 2, QTableWidgetItem(f"{det['precio_unitario']:.2f}"))
            self.table_detalles.setItem(i, 3, QTableWidgetItem(f"{det['descuento']:.2f}"))
            self.table_detalles.setItem(i, 4, QTableWidgetItem(f"{det['subtotal']:.2f}"))
            # Botón eliminar en la columna 5
            btn_elim = QPushButton("Eliminar")
            btn_elim.clicked.connect(lambda checked, row=i: self.eliminar_detalle(row))
            self.table_detalles.setCellWidget(i, 5, btn_elim)

    def agregar_detalle(self):
        # Diálogo para seleccionar producto y cantidad
        dialog = QDialog(self)
        dialog.setWindowTitle("Agregar Producto")
        layout = QFormLayout(dialog)

        producto_combo = QComboBox()
        productos = obtener_todos_productos() or []
        for p in productos:
            producto_combo.addItem(f"{p.nombre} (Stock: {p.stock})", p.id_producto)

        cantidad = QSpinBox()
        cantidad.setRange(1, 9999)
        precio = QDoubleSpinBox()
        precio.setRange(0, 999999.99)
        precio.setValue(0.0)
        descuento = QDoubleSpinBox()
        descuento.setRange(0, 999999.99)
        descuento.setValue(0.0)

        layout.addRow("Producto:", producto_combo)
        layout.addRow("Cantidad:", cantidad)
        layout.addRow("Precio unitario:", precio)
        layout.addRow("Descuento:", descuento)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted:
            prod_id = producto_combo.currentData()
            if prod_id is None:
                QMessageBox.warning(self, "Error", "Seleccione un producto.")
                return
            # Buscar nombre del producto
            prod_nombre = ""
            for p in productos:
                if p.id_producto == prod_id:
                    prod_nombre = p.nombre
                    break
            cant = cantidad.value()
            prec = precio.value()
            desc = descuento.value()
            subtotal = cant * prec - desc

            self.detalles_actuales.append({
                "id_detalle": None,  # nuevo detalle, sin ID
                "producto_id": prod_id,
                "producto_nombre": prod_nombre,
                "cantidad": cant,
                "precio_unitario": prec,
                "descuento": desc,
                "subtotal": subtotal
            })
            self.refrescar_tabla_detalles()

    def eliminar_detalle(self, row):
        if 0 <= row < len(self.detalles_actuales):
            confirm = QMessageBox.question(
                self, "Confirmar",
                f"¿Eliminar el producto '{self.detalles_actuales[row]['producto_nombre']}'?",
                QMessageBox.Yes | QMessageBox.No
            )
            if confirm == QMessageBox.Yes:
                # Si el detalle ya existe en BD, lo eliminamos físicamente
                det_id = self.detalles_actuales[row].get("id_detalle")
                if det_id:
                    try:
                        eliminar_detalle_fisico(det_id)
                    except Exception as e:
                        QMessageBox.critical(self, "Error", f"No se pudo eliminar detalle: {e}")
                        return
                del self.detalles_actuales[row]
                self.refrescar_tabla_detalles()

    def eliminar_detalle_seleccionado(self):
        current_row = self.table_detalles.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Seleccionar", "Seleccione un detalle para eliminar.")
            return
        self.eliminar_detalle(current_row)

    def aceptar(self):
        # Validar descuento total
        try:
            descuento_total = float(self.descuento_total.text()) if self.descuento_total.text() else 0.0
        except ValueError:
            QMessageBox.warning(self, "Error", "El descuento total debe ser un número.")
            return

        # Validar usuario
        usuario_id = self.usuario_combo.currentData()
        if usuario_id == -1 or usuario_id is None:
            QMessageBox.warning(self, "Error", "Seleccione un usuario válido.")
            return

        # Construir datos del pedido
        datos_pedido = {
            "usuario_id": usuario_id,
            "estado": self.estado_combo.currentText(),
            "metodo_pago": self.metodo_pago.text() or None,
            "fecha_entrega": self.fecha_entrega.date().toPython() if self.fecha_entrega.date() else None,
            "comentarios": self.comentarios.toPlainText() or None,
            "descuento_total": descuento_total
        }

        try:
            # Guardar o actualizar pedido
            if self.pedido is None:
                pedido_creado = crear_pedido(**datos_pedido)
                pedido_id = pedido_creado.id_pedido
            else:
                actualizar_pedido(self.pedido.id_pedido, **datos_pedido)
                pedido_id = self.pedido.id_pedido

            # Guardar detalles: para edición, primero eliminar todos los existentes y recrear
            # (o implementar lógica de upsert). Usamos eliminar y recrear por simplicidad.
            if self.pedido is not None:
                # Eliminar detalles existentes en BD
                eliminar_detalles_por_pedido(pedido_id)
                # Los detalles_actuales pueden tener id_detalle antiguo, pero lo ignoramos
                # porque vamos a recrearlos todos
                for det in self.detalles_actuales:
                    # Quitamos el id_detalle si existe para no pasarlo al crear
                    det.pop("id_detalle", None)
                    crear_detalle(
                        pedido_id=pedido_id,
                        producto_id=det["producto_id"],
                        cantidad=det["cantidad"],
                        precio_unitario=det["precio_unitario"],
                        descuento_aplicado=det["descuento"]
                    )
            else:
                # Nuevo pedido: guardar detalles directamente
                for det in self.detalles_actuales:
                    crear_detalle(
                        pedido_id=pedido_id,
                        producto_id=det["producto_id"],
                        cantidad=det["cantidad"],
                        precio_unitario=det["precio_unitario"],
                        descuento_aplicado=det["descuento"]
                    )

            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el pedido: {e}")
