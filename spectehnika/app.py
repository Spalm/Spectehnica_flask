from flask import Flask

from auth.manager import login_manager
from auth.views import bp as auth_bp
from core.views import bp as core_bp
from admin.views import bp as admin_bp
from emp.views import bp as emp_bp
from tehnika.views import bp as teh_bp

app = Flask(__name__)
app.secret_key = 'b52f2d8e8500810394e55ec5b6eae445d96164786b516bb2010315a6b07962febce1db8accb0e9965258844a9d846d74'
login_manager.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(core_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(emp_bp)
app.register_blueprint(teh_bp)

if __name__ == '__main__':
    app.run()
