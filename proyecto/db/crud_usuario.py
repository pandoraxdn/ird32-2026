from db.models import Usuario
from db.database import get_session
from datetime import date

def crear_usuario(nombre, email, telefono=None, direccion=None, fecha_nacimiento=None, activo=True):
    db = get_session()
    try:
        if isinstance(fecha_nacimiento, str):
            fecha_nacimiento = date.fromisoformat(fecha_nacimiento)
        nuevo = Usuario(
            nombre=nombre,
            email=email,
            telefono=telefono,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            activo=activo
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

def obtener_usuario_por_id(usuario_id):
    db = get_session()
    try:
        return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    finally:
        db.close()

def obtener_usuario_por_email(email):
    db = get_session()
    try:
        return db.query(Usuario).filter(Usuario.email == email).first()
    finally:
        db.close()

def obtener_usuarios_activos():
    db = get_session()
    try:
        return db.query(Usuario).filter(Usuario.activo == True).all()
    finally:
        db.close()

def obtener_usuarios_inactivos():
    db = get_session()
    try:
        return db.query(Usuario).filter(Usuario.activo == False).all()
    finally:
        db.close()

def obtener_todos_usuarios():
    db = get_session()
    try:
        return db.query(Usuario).all()
    finally:
        db.close()

def actualizar_usuario(usuario_id, **kwargs):
    db = get_session()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
        if not usuario:
            return None
        if 'fecha_nacimiento' in kwargs and isinstance(kwargs['fecha_nacimiento'], str):
            kwargs['fecha_nacimiento'] = date.fromisoformat(kwargs['fecha_nacimiento'])
        for key, value in kwargs.items():
            if hasattr(usuario, key):
                setattr(usuario, key, value)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_usuario_fisico(usuario_id):
    db = get_session()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
        if not usuario:
            return False
        db.delete(usuario)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_usuario_logico(usuario_id):
    return actualizar_usuario(usuario_id, activo=False)
