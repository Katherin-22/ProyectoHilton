import pymysql.cursors 

def obtener_categorias(connection):
    """
    Obtiene la lista de categorías disponibles desde la tabla Categoria.
    """
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT idCategoria, nombre FROM Categoria")
        categorias = cursor.fetchall()
        cursor.close()
        return categorias
    except Exception as e:
        print("Error al obtener categorías:", e)
        return []


def insertar_hotel(connection, nombre, descripcion, fecha, direccion, ciudad, pais, telefono, correo, id_categoria):
    """
    Inserta un nuevo hotel en la tabla hotel con estado 'abierto'.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO hotel (
                Nombre_Hotel, Descripcion, Fecha_apertura, Direccion,
                ciudad, Pais, Telefono_contacto, correo_electronico,
                idCategoria, estado
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'abierto')
        """, (nombre, descripcion, fecha, direccion, ciudad, pais, telefono, correo, id_categoria))
        connection.commit()
        cursor.close()
    except Exception as e:
        print("Error al insertar hotel:", e)


def obtener_hoteles(connection):
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT h.idHotel, h.Nombre_Hotel, h.Descripcion, h.Fecha_apertura, 
                       h.Direccion, h.ciudad, h.Pais, h.Telefono_contacto, 
                       h.correo_electronico, h.estado, c.nombre AS categoria_nombre
                FROM hotel h
                LEFT JOIN categoria c ON h.idCategoria = c.idCategoria
                WHERE h.estado = 'abierto'
            """)
            return cursor.fetchall()
    except Exception as e:
        print("Error al obtener hoteles:", e)
        return []


def ocultar_hoteles(connection, lista_ids):
    """
    Cambia el estado de los hoteles dados a 'cerrado' (ocultarlos sin eliminarlos).
    """
    try:
        cursor = connection.cursor()
        query = "UPDATE hotel SET estado = 'cerrado' WHERE idHotel IN ({})".format(
            ','.join(['%s'] * len(lista_ids))
        )
        cursor.execute(query, lista_ids)
        connection.commit()
        cursor.close()
    except Exception as e:
        print("Error al ocultar hoteles:", e)


def obtener_hotel_por_id(connection, id_hotel):
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""
            SELECT idHotel, Nombre_Hotel, Descripcion, Fecha_apertura,
                   Direccion, ciudad, Pais, Telefono_contacto,
                   correo_electronico, idCategoria
            FROM hotel
            WHERE idHotel = %s
        """, (id_hotel,))
        hotel = cursor.fetchone()
        cursor.close()
        return hotel
    except Exception as e:
        print("Error al obtener hotel por ID:", e)
        return None


def editar_hotel(connection, id_hotel, nombre, descripcion, fecha, direccion, ciudad, pais, telefono, correo, id_categoria):
    """
    Actualiza los datos de un hotel existente basado en su ID.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE hotel SET 
                Nombre_Hotel = %s,
                Descripcion = %s,
                Fecha_apertura = %s,
                Direccion = %s,
                ciudad = %s,
                Pais = %s,
                Telefono_contacto = %s,
                correo_electronico = %s,
                idCategoria = %s
            WHERE idHotel = %s
        """, (nombre, descripcion, fecha, direccion, ciudad, pais, telefono, correo, id_categoria, id_hotel))
        connection.commit()
        cursor.close()
    except Exception as e:
        print("Error al editar hotel:", e)
