from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.models import Machine, User, MachineTypes
from tehnika.forms import AddTehniks, AddType

bp = Blueprint('teh', __name__, url_prefix='/teh')


@bp.get('/tehnika')
def tehnika():
    type_form = AddType()
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
        'form': form,
        'type_form': type_form
    }
    return render_template('teh/tehnika.html', **context)


@bp.post('/add_tehnika')
def add_tehnika():
    type_form = AddType()
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
        'form': form,
        'type_form': type_form
    }
    return render_template('teh/tehnika.html', **context)


@bp.post('/add_type')
def add_type():
    form_type = AddType(request.form)
    title = form_type['title'].data
    # new_type = MachineTypes()
    # form.populate_obj(new_type)
    # new_type.save()
    """Не срабатывает валидация на форме"""
    MachineTypes.create(title=title)

    type_form = AddType()
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
        'form': form,
        'type_form': type_form
    }

    return render_template('teh/tehnika.html', **context)
