def registrar_usuario(connection, nombre, correo_usuario, contraseña, origen):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO usuario (nombre, correo_usuario, contraseña, origen) 
            VALUES (%s, %s, %s, %s)
        """, (nombre, correo_usuario, contraseña, origen))
        connection.commit()
        cursor.close()
    except Exception as e:
        print("Error al insertar usuario:", e)

# app/models/user_model.py

def obtener_usuario_por_correo(connection, correo, contraseña):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM usuario WHERE correo_usuario = %s AND contraseña = %s",
            (correo, contraseña)
        )
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
    except Exception as e:
        print("Error al consultar usuario:", e)
        return None

def get_user_by_id(connection, id_usuario):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_usuario,nombre, correo_usuario, contraseña, origen FROM usuarios WHERE id=%s", (id_usuario,))
        return cursor.fetchone()