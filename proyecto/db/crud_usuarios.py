from models import Usuario
from database import Sesion

def crear_usuario(nombre, email, telefono=None, direccion=None, fecha_nacimiento=None, activo=True):
    db = Sesion()
    try:
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

# -------------------- READ --------------------
def obtener_usuario_por_id(usuario_id):
    """
    SQL equivalente:
    SELECT * FROM usuarios WHERE id = usuario_id;
    """
    db = Sesion()
    try:
        return db.query(Usuario).filter(Usuario.id == usuario_id).first()
    finally:
        db.close()

def obtener_usuarios_activos():
    """
    SQL equivalente:
    SELECT * FROM usuarios WHERE activo = True;
    """
    db = SessionLocal()
    try:
        return db.query(Usuario).filter(Usuario.activo == True).all()
    finally:
        db.close()

def obtener_usuarios_inactivos():
    """
    SQL equivalente:
    SELECT * FROM usuarios WHERE activo = False;
    """
    db = SessionLocal()
    try:
        return db.query(Usuario).filter(Usuario.activo == False).all()
    finally:
        db.close()

def obtener_usuario_por_email(email):
    """
    SQL equivalente:
    SELECT * FROM usuarios WHERE email = 'email';
    """
    db = SessionLocal()
    try:
        return db.query(Usuario).filter(Usuario.email == email).first()
    finally:
        db.close()

def obtener_todos_usuarios():
    """
    SQL equivalente:
    SELECT * FROM usuarios;
    """
    db = SessionLocal()
    try:
        return db.query(Usuario).all()
    finally:
        db.close()

# -------------------- UPDATE --------------------
def actualizar_usuario(usuario_id, nombre=None, email=None, telefono=None, direccion=None,
                       fecha_nacimiento=None, activo=None):
    """
    SQL equivalente:
    UPDATE usuarios
    SET nombre = COALESCE(nombre, nombre),
        email = COALESCE(email, email),
        ...
    WHERE id = usuario_id;
    """
    db = Sesion()
    try:
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            return None
        if nombre is not None:
            usuario.nombre = nombre
        if email is not None:
            usuario.email = email
        if telefono is not None:
            usuario.telefono = telefono
        if direccion is not None:
            usuario.direccion = direccion
        if fecha_nacimiento is not None:
            usuario.fecha_nacimiento = fecha_nacimiento
        if activo is not None:
            usuario.activo = activo
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# -------------------- DELETE --------------------
def eliminar_usuario_fisico(usuario_id):
    """
    SQL equivalente:
    DELETE FROM usuarios WHERE id = usuario_id;
    (CASCADE borrará pedidos y detalles asociados)
    """
    db = Sesion()
    try:
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if usuario:
            db.delete(usuario)
            db.commit()
            return True
        return False
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def eliminar_usuario_logico(usuario_id):
    """
    SQL equivalente:
    UPDATE usuarios SET activo = False WHERE id = usuario_id;
    """
    return actualizar_usuario(usuario_id, activo=False)
