# app/__init__.py
from flask import Flask , g , current_app
import pymysql.cursors
from config import Config

#from app.config import Config  # Asegúrate que 'config.py' esté dentro de /app
import os

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración desde el archivo .env a través de config.py
    app.config.from_object(Config)

    # Conexión a la base de datos MySQL (sin ORM)
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

    # Guardar conexión como atributo de la app
    app.connection = connection

    # importar Blueprints
    from app.controllers.main_controller import main_bp
    from app.controllers.hotel_controller import hotel_bp
    from app.controllers.categoria_controller import categoria_bp 
    from app.controllers.administracion_controller import admin_bp
    from app.controllers.user_controller import user_bp


    # Registrar Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(user_bp)

    @app.teardown_appcontext
    def close_connection(exception=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    return app

def get_connection():
    """Obtiene una conexión MySQL y la guarda en el contexto global 'g'."""
    if 'db' not in g:
        g.db = pymysql.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB'],
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db