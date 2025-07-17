from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from app import get_connection
from app.models.user_model import registrar_usuario, obtener_usuario_por_correo
from app.models.categoria_model import get_categoria_count
from app.models.hoteles_model import get_hotel_count
from app.models.user_model import get_user_by_id

user_bp = Blueprint('user', __name__)

# FORMULARIO DE REGISTRO
@user_bp.route('/registro', methods=['GET'])
def mostrar_formulario_registro():
    return render_template('cuenta/registro_usuario.html')

# ACCIÓN DE REGISTRAR
@user_bp.route('/registrar_usuario', methods=['POST'])
def registrar_usuario_route():
    connection = get_connection()
    
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contrasena']
        origen = request.form['origen']

        registrar_usuario(connection, nombre, correo, contraseña, origen)
        flash('Usuario registrado correctamente. Ahora inicia sesión.', 'success')
        return redirect(url_for('user.login'))

    except Exception as e:
        flash('Error al registrar usuario: ' + str(e), 'danger')
        return redirect(url_for('user.mostrar_formulario_registro'))

# INICIO DE SESIÓN
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    connection = get_connection()

    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        usuario = obtener_usuario_por_correo(connection, correo, contrasena)

        if usuario:
            session['usuario'] = usuario  # Guarda el usuario en sesión
            flash(f'Bienvenido, {usuario["nombre"]}', 'success')
            return redirect(url_for('user.administracion'))  # redirige al dashboard
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return redirect(url_for('user.login'))

    return render_template('cuenta/inicio_sesion.html')  # Esto es GET, debe mostrar el login


@user_bp.route('/hoteles')
def hoteles():
    return render_template('GestionHoteles/hoteles.html')

from flask import Blueprint, redirect, url_for, session, flash

@user_bp.route('/logout')
def logout():
    session.clear() 
    flash('Sesión cerrada exitosamente', 'info')
    return redirect(url_for('user.login'))  

@user_bp.route('/administracion')
def administracion():

    connection = current_app.connection

    # estadísticas del sistema
    categoria_count = get_categoria_count(connection)
    hotel_count = get_hotel_count(connection)

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS user_count FROM usuario")
        user_count = cursor.fetchone()['user_count']

    return render_template('administracion/administracion.html', 
                           user_count=user_count,
                           categoria_count=categoria_count,
                           hotel_count=hotel_count)
