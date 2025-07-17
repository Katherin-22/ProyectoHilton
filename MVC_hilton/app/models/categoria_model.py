# para ver todas las categorias
def get_todas_categorias(conection):
    with conection.cursor() as cursor:
        cursor.execute("SELECT * FROM Categoria")
        return cursor.fetchall()
# para insertar una categoria
def insert_categoria(connection,nombre, tipo, descripcion, servicio):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Categoria (nombre,tipo,descripcion,servicio) VALUES (%s, %s, %s, %s)",
            (nombre, tipo, descripcion, servicio)
        )
        connection.commit()
    
def delete_categoria(connection, idCategoria):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Categoria WHERE idCategoria=%s", (idCategoria,))
        connection.commit()

def update_categoria(connection, idCategoria,nombre, tipo, descripcion, servicio):
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE categoria 
            SET nombre=%s, tipo=%s, descripcion=%s, servicio=%s 
            WHERE idCategoria=%s
        """, (nombre, tipo, descripcion, servicio,idCategoria))
        connection.commit()
# para ver una categoria
def get_categoria_por_id(conection,idCategoria):
    with conection.cursor() as cursor:
        cursor.execute("SELECT * FROM Categoria WHERE idCategoria = %s", (idCategoria,))
        return cursor.fetchone()

# para contar las categorias
def get_categoria_count(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS categoria_count FROM Categoria")
        return cursor.fetchone()['categoria_count']