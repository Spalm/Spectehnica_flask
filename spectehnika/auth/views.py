from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import login_user, logout_user, login_required, current_user

from auth.forms import LoginForm
from auth.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.get('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@bp.post('/login')
def login_post():
    form = LoginForm(request.form)
    if not form.validate():
        return render_template('auth/login.html', form=form)

    user = User.get(email=form.email.data)
    login_user(user)
    return redirect(url_for('core.main'))


@bp.get('/logout')
@login_required
def logout():
    form = LoginForm(request.form)
    return render_template('auth/login.html', form=form)
