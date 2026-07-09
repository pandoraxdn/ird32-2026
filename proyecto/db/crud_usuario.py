from db.models import Usuario
from db.database import Sesion

def crear_usuario(nombre, email, telefono, direccion, fecha_nacimiento, activo=True):
    db = Sesion()
    try:
        registro = Usuario(
            nombre = nombre,
            email = email,
            telefono = telefono,
            direccion = direccion,
            fecha_nacimiento = fecha_nacimiento,
            activo = activo
        )
        db.add(registro)
        db.commit() 
        db.refresh(registro) 
        return registro
    except Exception as e:
        db.rollback()
        print(f"Error al crear usuario: {e}")
        return None          
    finally:
        db.close()       

def buscar_usuario_id(id_usuario):
    db = Sesion()
    try:
        return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    except Exception as e:
        raise e
    finally:
        db.close()
        
def lista_usuarios():
    db = Sesion()
    try:
        users = db.query(Usuario).all()
        return users
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        db.close()
        
def actualizar_usuario(id_usuario, nombre, email, telefono, direccion, fecha_nacimiento, activo):
    db = Sesion()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if usuario:
            usuario.nombre = nombre
            usuario.email = email
            usuario.telefono = telefono
            usuario.direccion = direccion
            usuario.fecha_nacimiento = fecha_nacimiento
            usuario.activo = activo
            db.commit()
            db.refresh(usuario)
            return usuario
    except Exception as e:
        raise e
    finally:
        db.close()
        
def eliminar_usuario(id_usuario):
    db = Sesion()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if usuario:
            db.delete(usuario)
            db.commit()
            return usuario
    except Exception as e:
        raise e
    finally:
        db.close()
