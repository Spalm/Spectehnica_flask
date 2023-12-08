from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.models import Machine, User, MachineTypes, Owner
from tehnika.forms import AddTehniks, AddType

bp = Blueprint('teh', __name__, url_prefix='/teh')


@bp.get('/tehnika')
def tehnika():
    type_form = AddType()
    form = AddTehniks()
    tehniks = Machine.select().join(User).where(Machine.owner == 1)

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
    tehniks = Machine.select().join(User).where(Machine.owner == 1)

    context = {
        'tehniks': tehniks,
        'form': form,
        'type_form': type_form
    }

    if not form.validate():
        return render_template('teh/tehnika.html', **context)

    model = form['model'].data
    number = form['number'].data
    type_id = form['type'].data
    user_id = form['user'].data
    owner_id = 1
    Machine.create(model=model, number=number, type=type_id, user=user_id, owner=owner_id)

    flash('Машина успешно добавлена')
    return redirect(url_for('teh.tehnika'))


@bp.post('/add_type')
def add_type():
    type_form = AddType(request.form)
    form = AddTehniks(request.form)
    tehniks = Machine.select().join(User).where(Machine.owner == 1)
    context = {
        'tehniks': tehniks,
        'form': form,
        'type_form': type_form
    }
    if not type_form.validate():
        return render_template('teh/tehnika.html', **context)
    title = type_form['title'].data
    # new_type = MachineTypes()
    # form.populate_obj(new_type)
    # new_type.save()
    MachineTypes.create(title=title)

    type_form = AddType()
    form = AddTehniks()
    tehniks = Machine.select(Machine.model, Machine.user, Machine.number).join(User).where(Machine.owner == 1)

    context = {
        'tehniks': tehniks,
        'form': form,
        'type_form': type_form
    }
    flash('Новый тип создан')
    return redirect(url_for('teh.tehnika'))


@bp.delete('del_tehnika/<int:id>')
def del_tehnika(id):
    Machine.delete_by_id(id)
    return ''
