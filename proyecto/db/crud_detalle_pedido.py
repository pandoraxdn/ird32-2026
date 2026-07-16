from db.models import DetallePedido, Producto
from db.database import get_session

def crear_detalle(pedido_id, producto_id, cantidad, precio_unitario, descuento_aplicado=0.0):
    db = get_session()
    try:
        subtotal = cantidad * precio_unitario - descuento_aplicado
        nuevo = DetallePedido(
            pedido_id=pedido_id,
            producto_id=producto_id,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            descuento_aplicado=descuento_aplicado,
            subtotal=subtotal
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

def obtener_detalle_por_id(detalle_id):
    db = get_session()
    try:
        return db.query(DetallePedido).filter(DetallePedido.id_detalle_producto == detalle_id).first()
    finally:
        db.close()

def obtener_detalles_por_pedido(pedido_id):
    db = get_session()
    try:
        return db.query(DetallePedido).filter(DetallePedido.pedido_id == pedido_id).all()
    finally:
        db.close()

def obtener_detalles_por_producto(producto_id):
    db = get_session()
    try:
        return db.query(DetallePedido).filter(DetallePedido.producto_id == producto_id).all()
    finally:
        db.close()

def obtener_todos_detalles():
    db = get_session()
    try:
        return db.query(DetallePedido).all()
    finally:
        db.close()

def actualizar_detalle(detalle_id, **kwargs):
    db = get_session()
    try:
        detalle = db.query(DetallePedido).filter(DetallePedido.id_detalle_producto == detalle_id).first()
        if not detalle:
            return None
        for key, value in kwargs.items():
            if hasattr(detalle, key):
                setattr(detalle, key, value)
        # Recalcular subtotal si se modificó cantidad, precio o descuento
        if 'cantidad' in kwargs or 'precio_unitario' in kwargs or 'descuento_aplicado' in kwargs:
            detalle.subtotal = detalle.cantidad * detalle.precio_unitario - detalle.descuento_aplicado
        db.commit()
        db.refresh(detalle)
        return detalle
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_detalle_fisico(detalle_id):
    db = get_session()
    try:
        detalle = db.query(DetallePedido).filter(DetallePedido.id_detalle_producto == detalle_id).first()
        if not detalle:
            return False
        db.delete(detalle)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_detalles_por_pedido(pedido_id):
    """Elimina todos los detalles de un pedido específico."""
    db = get_session()
    try:
        detalles = db.query(DetallePedido).filter(DetallePedido.pedido_id == pedido_id).all()
        for detalle in detalles:
            db.delete(detalle)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
