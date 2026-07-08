from models import Producto
from database import Sesion

def crear_producto(nombre, precio, stock, descripcion, categoria, proveedor, peso_kg, dimensiones):
    db = Sesion()
    try:
        registro = Producto(
            nombre = nombre,
            precio = precio,
            stock = stock,
            descripcion = descripcion,
            categoria = categoria,
            proveedor = proveedor,
            peso_kg = peso_kg,
            dimensiones = dimensiones
        )
        db.add(registro)
        db.commit()
        db.refresh(registro)
        return registro
    except Exception as e:
        raise e
    finally:
        db.close()
        
def buscar_id_producto(id_producto):
    db = Sesion()
    try:
        return db.query(Producto).filter(Producto.id_producto == id_producto).first()
    except Exception as e:
        raise e
    finally:
        db.close()
        
def actualizar_producto(id_producto, nombre, precio, stock, descripcion, categoria, proveedor, peso_kg, dimensiones):
    db = Sesion()
    try:
        producto = db.query(Producto).filter(Producto.id_producto == id_producto).first()
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.descripcion = descripcion
        producto.categoria = categoria
        producto.proveedor = proveedor
        producto.peso_kg = peso_kg
        producto.dimensiones = dimensiones
        db.commit()
        db.refresh(producto)
        return producto
    except Exception as e:
        raise e
    finally:
        db.close()
        
def eliminar_producto(id_producto):
    db = Sesion()
    try:
        producto = db.query(Producto).filter(Producto.id_producto == id_producto).first()
        if producto:
            db.delete(producto)
            db.commit()
            return producto
    except Exception as e:
        raise e
    finally:
        db.close()