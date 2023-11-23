from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from emp.forms import Employee
from auth.models import User, Role

bp = Blueprint('emp', __name__, url_prefix='/emp')


@bp.get('/employees')
def employees():
    form = Employee()
    users = User.select(User.name, User.role).join(Role)
    context = {
        'users': users,
        'form': form
    }
    return render_template('emp/employees.html', **context)
