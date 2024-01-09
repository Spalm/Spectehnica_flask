from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.models import Machine, User, MachineTypes, Owner
from tehnika.forms import AddTehniks, AddType

bp = Blueprint('teh', __name__, url_prefix='/teh')


@bp.get('/tehnika')
@login_required
def tehnika():
    type_form = AddType()
    form = AddTehniks()
    tehniks = Machine.select().join(User).where(Machine.owner == 1).order_by(Machine.id)

    context = {
        'tehniks': tehniks,
        'form': form,
        'type_form': type_form
    }
    return render_template('teh/tehnika.html', **context)


# @bp.get('/tehnika_form')
# def tehnika_form():
#     form = AddTehniks()
#     return render_template('teh/tehnika_form.html', form=form)


@bp.post('/add_tehnika')
def add_tehnika():
    form = AddTehniks(request.form)

    if not form.validate():
        form.model.data = ''
        form.user.data = ''
        return render_template('teh/tehnika_form.html', form=form)

    model = form.model.data
    number = form.number.data
    type_id = int(form.type.data)
    user_id = int(form.user.data)
    owner_id = 1
    Machine.create(model=model, number=number, type=type_id, user=user_id, owner=owner_id)

    form.model.data = ''
    form.number.data = ''
    return render_template('teh/tehnika_form.html', form=form, show_success_message=1)


@bp.get('/type_form')
def type_form():
    type_form = AddType()
    render_template('teh/type_form.html', type_form=type_form)


@bp.post('/add_type')
def add_type():
    type_form = AddType(request.form)
    if not type_form.validate():
        type_form.title.data = ''
        return render_template('teh/type_form.html', type_form=type_form)
    new_type = MachineTypes()
    type_form.populate_obj(new_type)
    new_type.save()
    type_form.title.data = ''
    return render_template('teh/type_form.html', type_form=type_form, show_success_mesage=1)


@bp.get('machine/<int:id>')
def row_machine(id: int):
    context = {
        'tehnika': Machine.get_by_id(id)
    }
    return render_template('teh/row_machine.html', **context)


@bp.delete('del_tehnika/<int:id>')
def del_tehnika(id: int):
    Machine.delete_by_id(id)
    return ''


@bp.get('machine/<int:id>/edit')
def get_edit_row(id: int):
    context = {
        'tehnika': Machine.get_by_id(id)
    }
    return render_template('teh/edit_machine.html', **context)


@bp.put('machine/<int:id>')
def put_edit_row(id: int):
    machine = Machine.get_by_id(id)
    machine.model = request.form['model']
    machine.user = request.form['user']
    machine.number = request.form['number']
    machine.save()

    context = {
        'tehnika': Machine.get_by_id(id)
    }
    return render_template('teh/row_machine.html', **context)
