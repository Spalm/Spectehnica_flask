from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.forms import LoginForm
from auth.models import Machine, User
from core.forms import ReportForm

bp = Blueprint('admin1', __name__, url_prefix='/admin1')


@bp.get('/administration')
def administration():
    form = ReportForm()
    return render_template('admin/administration.html', form=form)


