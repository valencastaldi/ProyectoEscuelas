from flask import Flask
from auth.routes import auth_bp
from admin.routes import admin_bp
from profesor.routes import profesor_bp
from alumno.routes import alumno_bp
from comunicados.routes import comunicados_bp

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'clave_secreta_para_sesiones'

# Registrar Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(profesor_bp, url_prefix='/profesor')
app.register_blueprint(alumno_bp, url_prefix='/alumno')
app.register_blueprint(comunicados_bp, url_prefix='/comunicados')

if __name__ == '__main__':
    app.run(debug=True)