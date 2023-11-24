from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.models import Machine, User, MachineTypes
from tehnika.forms import AddTehniks

bp = Blueprint('teh', __name__, url_prefix='/teh')


@bp.get('/tehnika')
def tehnika():
    form = AddTehniks()
    tehniks = Machine.select(Machine.model, Machine.user, Machine.number).join(User).where(Machine.owner == 1)
    context = {
        'tehniks': tehniks,
        'form': form
    }
    return render_template('teh/tehnika.html', **context)
