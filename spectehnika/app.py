import os
from pathlib import Path

import dotenv
from flask import Flask, redirect, url_for

from admin.views import bp as admin_bp
from auth.manager import login_manager
from auth.views import bp as auth_bp
from cli import register_cli_commands
from core.views import bp as core_bp
from db import db
from emp.views import bp as emp_bp
from reports.views import bp as rep_bp
from tehnika.views import bp as teh_bp


def index():
    return redirect(url_for('auth.login'))


def create_app(config_name: str = 'Config', env_file: str = '.env') -> Flask:
    dotenv.load_dotenv(Path().resolve() / env_file)
    import config

    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    db.init(
        database=app.config['DB_NAME'],
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD']
    )
    login_manager.init_app(app)
    app.add_url_rule('/', view_func=index)
    app.register_blueprint(auth_bp)
    app.register_blueprint(core_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(emp_bp)
    app.register_blueprint(teh_bp)
    app.register_blueprint(rep_bp)
    register_cli_commands(app)
    return app
