from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    direccion = Column(String(200), nullable=True)
    fecha_nacimiento = Column(String(200), nullable=True)
    activo = Column(Boolean, default=True)
    registrado_en = Column(DateTime, default=datetime.now())
    pedidos = relationship("Pedido", back_populates="usuario", cascade="all, delete")

class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(500), nullable=True)
    categoria = Column(String(50), nullable=True)
    proveedor = Column(String(100), nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    peso_kg = Column(Float, nullable=True)
    dimensiones = Column(String(50), nullable=True)
    fecha_alta = Column(Date, default=date.today)
    detalles = relationship("DetallePedido", back_populates="producto")

class Pedido(Base):
    __tablename__ = "pedidos"
    id_pedido = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    fecha_pedido = Column(DateTime, default=datetime.now())
    estado = Column(String(50), default="PENDIENTE")
    metodo_pago = Column(String(50), nullable=True)
    fecha_entrega = Column(Date, nullable=True)
    comentarios = Column(String(300), nullable=True)
    descuento_total = Column(Float, default=0.0)
    usuario = relationship("Usuario", back_populates="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido", cascade="all, delete")

class DetallePedido(Base):
    __tablename__ = "detalles_pedido"
    id_detalle_producto = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id_pedido"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id_producto"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    descuento_aplicado = Column(Float, default=0.0)
    subtotal = Column(Float, nullable=False)
    pedido = relationship("Pedido", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles")
