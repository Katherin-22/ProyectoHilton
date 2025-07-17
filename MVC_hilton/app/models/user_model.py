import pymysql

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

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='tu_contraseña',
        database='HotelHilton',
        cursorclass=pymysql.cursors.DictCursor
    )

def get_user_by_id(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM usuario WHERE id = %s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
        return result
    except Exception as e:
        print("Error al obtener usuario por ID:", e)
        return None
    finally:
        connection.close()