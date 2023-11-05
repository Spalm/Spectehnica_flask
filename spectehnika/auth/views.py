from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.forms import LoginForm
from auth.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.get('/login')
def login():
    form = LoginForm()
    context = {
        'form': form
    }
    return render_template('auth/login.html', **context)


# @bp.post('/login')
# def login():
#     form = LoginForm(request.form)
#     user = User.get_or_none((User.email == form['email']) & (User.password == form['password']))
#     if user is None:
#         return redirect(url_for('login'))
#     else:
#         return redirect('auth/home_page.html')


@bp.get('/user_home_page')
def home_page():
    return render_template('user/user_home_page.html')