from datetime import datetime, date

from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from emp.forms import Employee
from auth.models import User, Role, MachineTypes

bp = Blueprint('emp', __name__, url_prefix='/emp')


@bp.get('/employees')
@login_required
def employees():
    form = Employee()
    roles = Role.select(Role.id, Role.title)
    role_choises = [(role.id, role.title) for role in roles]
    form.role.choices = role_choises
    context = {
        'current_user': current_user,
        'form': form
    }
    return render_template('emp/employees.html', **context)


# @bp.get('/employee_form')
# def employee_form():
#     form = Employee()
#     render_template('emp/employee_form.html', form=form)


@bp.post('/employee')
def add_employee():
    form = Employee(request.form)
    if not form.validate():
        form.name.data = ''
        form.email.data = ''
        form.password.data = ''
        return render_template('emp/employee_form.html', form=form)

    name = form['name'].data
    role = form['role'].data
    email = form['email'].data
    password = form['password'].data
    creation_date = date.today()
    User.create(name=name, email=email, password=password, creation_date=creation_date,
                role=role, is_admin=False)
    form = Employee()
    return render_template('emp/employee_form.html', form=form, show_success_message=1)


