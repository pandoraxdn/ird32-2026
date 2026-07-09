from db.crud_usuario import lista_usuarios

if __name__ == "__main__":

    """
    user = crear_usuario(
            nombre="Juanito",
            email="juanito@gmail.com",
            telefono="7222245781",
            direccion="5 de mayo #105",
            fecha_nacimiento="2026-07-09")
    """

    usuarios = lista_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(f"""
                ID: {usuario.id_usuario}
                nombre: {usuario.nombre}
                telefono: {usuario.telefono}
                email: {usuario.email}
            """)
