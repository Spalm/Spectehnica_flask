from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.models import Machine, User, MachineTypes
from tehnika.forms import AddTehniks

bp = Blueprint('teh', __name__, url_prefix='/teh')


@bp.get('/tehnika')
def tehnika():
    form = AddTehniks()
    tehniks = Machine.select(Machine.model, Machine.user, Machine.number).join(User).where(Machine.owner == 1)

    users = User.select(User.id, User.name)
    users_choise = [(user.id, user.name) for user in users]
    form.user.choices = users_choise

    types = MachineTypes.select(MachineTypes.id, MachineTypes.title)
    types_choises = [(type_.id, type_.title) for type_ in types]
    form.type.choices = types_choises

    context = {
        'tehniks': tehniks,
        'form': form
    }
    return render_template('teh/tehnika.html', **context)


@bp.post('/addtehnika')
def addtehnika():
    form = AddTehniks(request.form)
    model = form['model'].data
    number = form['number'].data
    type_id = form['type'].data
    user_id = form['user'].data
    owner_id = 1
    Machine.create(model=model, number=number, type=type_id, user=user_id, owner=owner_id)

    tehniks = Machine.select(Machine.model, Machine.user, Machine.number).join(User).where(Machine.owner == 1)
    users = User.select(User.id, User.name)
    users_choise = [(user.id, user.name) for user in users]
    form.user.choices = users_choise

    types = MachineTypes.select(MachineTypes.id, MachineTypes.title)
    types_choises = [(type_.id, type_.title) for type_ in types]
    form.type.choices = types_choises

    context = {
        'tehniks': tehniks,
        'form': form
    }
    return render_template('teh/tehnika.html', **context)


