# app/controllers/admin_controller.py
from flask import Blueprint, render_template, session, redirect, url_for, current_app
from app.models.categoria_model import get_categoria_count
from app.models.hoteles_model import get_hotel_count
from app.models.user_model import get_user_by_id

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/administracion')
def administracion():

#    id_usuario = session.get('id_usuario')
#    if not id_usuario:
#       return redirect(url_for('user.login'))

    connection = current_app.connection
#    user = get_user_by_id(connection, id_usuario)
#    if not user:
#        return "Administrador no encontrado"

    # estadísticas del sistema
    categoria_count = get_categoria_count(connection)
    hotel_count = get_hotel_count(connection)

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS user_count FROM usuario")
        user_count = cursor.fetchone()['user_count']

    return render_template('administracion/administracion.html', 
                           #user=user,
                           user_count=user_count,
                           categoria_count=categoria_count,
                           hotel_count=hotel_count)

    

