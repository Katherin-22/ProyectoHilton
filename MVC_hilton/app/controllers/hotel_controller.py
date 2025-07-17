from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.hotel_model import (
    insertar_hotel, obtener_categorias, obtener_hoteles, ocultar_hoteles, obtener_hotel_por_id, editar_hotel)
from app import get_connection

hotel_bp = Blueprint('hotel', __name__)


@hotel_bp.route('/registrar_hotel', methods=['GET', 'POST'])
def registrar_hotel():
    connection = get_connection()

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        fecha = request.form.get('fecha')
        direccion = request.form.get('direccion')
        ciudad = request.form.get('ciudad')
        pais = request.form.get('pais')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        id_categoria = request.form.get('categoria')

        if not all([nombre, descripcion, fecha, direccion, ciudad, pais, telefono, correo, id_categoria]):
            flash("Todos los campos son obligatorios", "danger")
        else:
            try:
                insertar_hotel(
                    connection,
                    nombre,
                    descripcion,
                    fecha,
                    direccion,
                    ciudad,
                    pais,
                    telefono,
                    correo,
                    id_categoria
                )
                flash("Hotel registrado exitosamente", "success")
                return redirect(url_for('hotel.lista_hoteles'))
            except Exception as e:
                flash(f"Error al registrar hotel: {str(e)}", "danger")

    categorias = obtener_categorias(connection)
    return render_template('GestionHoteles/registrar_hotel.html', categorias=categorias, modo='crear')


@hotel_bp.route('/hoteles')
def lista_hoteles():
    connection = get_connection()
    hoteles = obtener_hoteles(connection)
    return render_template('GestionHoteles/hoteles.html', hoteles=hoteles)


@hotel_bp.route('/eliminar_hoteles', methods=['POST'])
def eliminar_hoteles():
    ids_str = request.form.get('ids_eliminar', '')
    if ids_str:
        ids = [int(id) for id in ids_str.split(',') if id.isdigit()]
        connection = get_connection()
        try:
            ocultar_hoteles(connection, ids)
            flash(f"{len(ids)} hotel(es) ocultado(s) exitosamente.", "success")
        except Exception as e:
            flash(f"Error al ocultar hoteles: {str(e)}", "danger")
    else:
        flash("No se seleccionaron hoteles para ocultar.", "warning")
    return redirect(url_for('hotel.lista_hoteles'))


@hotel_bp.route('/editar_hotel/<int:id>', methods=['GET', 'POST'])
def editar_hotel_view(id):
    connection = get_connection()
    hotel = obtener_hotel_por_id(connection, id)

    if not hotel:
        flash("Hotel no encontrado", "danger")
        return redirect(url_for('hotel.lista_hoteles'))

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        fecha = request.form.get('fecha')
        direccion = request.form.get('direccion')
        ciudad = request.form.get('ciudad')
        pais = request.form.get('pais')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        id_categoria = request.form.get('categoria')

        if not all([nombre, descripcion, fecha, direccion, ciudad, pais, telefono, correo, id_categoria]):
            flash("Todos los campos son obligatorios", "danger")
        else:
            try:
                editar_hotel(
                    connection,
                    id,
                    nombre,
                    descripcion,
                    fecha,
                    direccion,
                    ciudad,
                    pais,
                    telefono,
                    correo,
                    id_categoria
                )
                flash("Hotel editado exitosamente", "success")
                return redirect(url_for('hotel.lista_hoteles'))
            except Exception as e:
                flash(f"Error al editar hotel: {str(e)}", "danger")

    categorias = obtener_categorias(connection)
    return render_template(
        'GestionHoteles/registrar_hotel.html',
        categorias=categorias,
        hotel=hotel,
        modo='editar'
    )
