from db.models import Pedido
from db.database import get_session
from datetime import datetime

def crear_pedido(usuario_id, estado="PENDIENTE", metodo_pago=None,
                 fecha_entrega=None, comentarios=None, descuento_total=0.0):
    db = get_session()
    try:
        if isinstance(fecha_entrega, str):
            fecha_entrega = datetime.fromisoformat(fecha_entrega).date()
        nuevo = Pedido(
            usuario_id=usuario_id,
            estado=estado,
            metodo_pago=metodo_pago,
            fecha_entrega=fecha_entrega,
            comentarios=comentarios,
            descuento_total=descuento_total
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

def obtener_pedido_por_id(pedido_id):
    db = get_session()
    try:
        return db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
    finally:
        db.close()

def obtener_todos_pedidos():
    db = get_session()
    try:
        return db.query(Pedido).all()
    finally:
        db.close()

def obtener_pedidos_por_usuario(usuario_id):
    db = get_session()
    try:
        return db.query(Pedido).filter(Pedido.usuario_id == usuario_id).all()
    finally:
        db.close()

def obtener_pedidos_por_estado(estado):
    db = get_session()
    try:
        return db.query(Pedido).filter(Pedido.estado == estado).all()
    finally:
        db.close()

def actualizar_pedido(pedido_id, **kwargs):
    db = get_session()
    try:
        pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
        if not pedido:
            return None
        if 'fecha_entrega' in kwargs and isinstance(kwargs['fecha_entrega'], str):
            kwargs['fecha_entrega'] = datetime.fromisoformat(kwargs['fecha_entrega']).date()
        for key, value in kwargs.items():
            if hasattr(pedido, key):
                setattr(pedido, key, value)
        db.commit()
        db.refresh(pedido)
        return pedido
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_pedido_fisico(pedido_id):
    db = get_session()
    try:
        pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
        if not pedido:
            return False
        db.delete(pedido)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_pedido_logico(pedido_id):
    return actualizar_pedido(pedido_id, estado="CANCELADO")
