from datetime import datetime, date

from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from emp.forms import Employee
from auth.models import User, Role

bp = Blueprint('emp', __name__, url_prefix='/emp')


@bp.get('/employees')
@login_required
def employees():
    form = Employee()
    roles = Role.select(Role.id, Role.title)
    role_choises = [(role.id, role.title) for role in roles]
    form.role.choices = role_choises
    users = User.select(User.name, User.role).join(Role)
    context = {
        'users': users,
        'form': form
    }
    return render_template('emp/employees.html', **context)


@bp.post('/employees')
@login_required
def add_employees():
    form_data = Employee(request.form)
    if not form_data.validate():
        return render_template('emp/employees.html', form=form_data)

    name = form_data['name'].data
    email = form_data['email'].data
    password = form_data['password'].data
    creation_date = date.today()
    role = form_data['role'].data
    User.create(name=name, email=email, password=password, creation_date=creation_date,
                role=role, is_admin=False)

    flash('Пользователь успешно создан')
    return redirect(url_for('emp.employees'))

