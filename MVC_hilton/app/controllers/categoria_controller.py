from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import os

from app.models.categoria_model import (
    get_todas_categorias,
    insert_categoria,
    delete_categoria,
    update_categoria,
    get_categoria_por_id
)
categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/CategoriaHotel', methods=['GET'])
def ver_categoria():
    connection = current_app.connection
    categorias = get_todas_categorias(connection)
    return render_template('GestionCategorias/vistaCategoria.html', categorias=categorias)

@categoria_bp.route('/create_categoria', methods=['GET', 'POST'])
def crear_categoria():
    connection = current_app.connection

    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        servicio = request.form['servicio']

        try:
            insert_categoria(connection, nombre, tipo, descripcion, servicio)
            flash('Categoria creada exitosamente', 'success')
        except Exception as e:
            flash('Error al crear la categoria: ' + str(e), 'danger')

        return redirect(url_for('categoria_bp.ver_categoria'))

    return render_template('GestionCategorias/registroCategoria.html')

@categoria_bp.route('/procesar_accion', methods=['POST'])
def procesar_accion():
    connection = current_app.connection
    ids = request.form.getlist('categorias_seleccionadas')
    accion = request.form.get('accion')

    if not ids:
        flash("No seleccionaste ninguna categoría", "warning")
        return redirect(url_for('categoria_bp.ver_categoria'))

    try:
        if accion == "eliminar":
            for idCategoria in ids:
                delete_categoria(connection, idCategoria)
            flash("Categorías eliminadas exitosamente", "success")

        elif accion == "editar":
            if len(ids) > 1:
                flash("Solo puedes editar una categoría a la vez", "warning")
            else:
                return redirect(url_for('categoria_bp.editar_categoria', idCategoria=ids[0]))

    except Exception as e:
        flash("Error al procesar las categorías: " + str(e), "danger")

    return redirect(url_for('categoria_bp.ver_categoria'))


@categoria_bp.route('/editar_categoria/<int:idCategoria>', methods=['GET', 'POST'])
def editar_categoria(idCategoria):
    connection = current_app.connection

    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        servicio = request.form['servicio']

        try:
            update_categoria(connection, idCategoria, nombre, tipo, descripcion, servicio)
            flash('Usuario modificado exitosamente', 'success')
        except Exception as e:
            flash('Error al modificar el usuario: ' + str(e), 'danger')

        return redirect(url_for('categoria_bp.ver_categoria'))

# GET: mostrar formulario con datos actuales
    categoria = get_categoria_por_id(connection, idCategoria)  # Esta función debe traer 1 categoría
    return render_template('GestionCategorias/editarCategoria.html', categoria=categoria)
