from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register')
def register():
    return "Registrar Usuario"

@bp.route('/login')
def login():
    return "Iniciar sesión"
