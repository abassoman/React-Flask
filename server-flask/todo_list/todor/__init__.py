from flask import Flask
from flask-cors import CORS


def create_app():

    app = Flask(__name__)
    CORS(app) #enable CORS on all routes

    #Cofiguración del Proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = 'dev'
    )

    #Registrar Blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return 'Hola Mundo'
    
    @app.route('/api/users')
    def get_users():
            return {
                 'users': ['a', 'b', 'c']
            }

    return app