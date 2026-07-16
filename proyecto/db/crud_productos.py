from db.models import Producto
from db.database import get_session

def crear_producto(nombre, precio, stock, descripcion=None, categoria=None,
                   proveedor=None, peso_kg=None, dimensiones=None):
    db = get_session()
    try:
        nuevo = Producto(
            nombre=nombre,
            precio=precio,
            stock=stock,
            descripcion=descripcion,
            categoria=categoria,
            proveedor=proveedor,
            peso_kg=peso_kg,
            dimensiones=dimensiones
        )
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return nuevo
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def obtener_producto_por_id(producto_id):
    db = get_session()
    try:
        return db.query(Producto).filter(Producto.id_producto == producto_id).first()
    finally:
        db.close()

def obtener_todos_productos():
    db = get_session()
    try:
        return db.query(Producto).all()
    finally:
        db.close()

def actualizar_producto(producto_id, **kwargs):
    db = get_session()
    try:
        producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
        if not producto:
            return None
        for key, value in kwargs.items():
            if hasattr(producto, key):
                setattr(producto, key, value)
        db.commit()
        db.refresh(producto)
        return producto
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_producto_fisico(producto_id):
    db = get_session()
    try:
        producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
        if not producto:
            return False
        db.delete(producto)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
