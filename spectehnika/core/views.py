from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.forms import LoginForm
from auth.models import User, Owner, MachineTypes
from core.forms import ReportForm, DataForm, OwnerForm

from auth.models import Machine
from tehnika.forms import AddTehniks

bp = Blueprint('core', __name__, url_prefix='/core')


@bp.get('/main')
@login_required
def main():
    form = AddTehniks()
    form_owner = OwnerForm()
    data_form = DataForm()
    report_form = ReportForm()
    tehniks = Machine.select(Machine.model, Machine.user, Machine.number).join(User).where(Machine.owner == 1)

    context = {
        'form_owner': form_owner,
        'report_form': report_form,
        'data_form': data_form,
        'tehniks': tehniks,
        'form': form,
        'current_user': current_user
    }
    return render_template('core/main.html', **context)


@bp.get('/owners')
def owners():
    owner_id = int(request.args.get('owner'))
    machines = Machine.select(Machine.id, Machine.model)
    if owner_id:
        machines = machines.where(Machine.owner_id == owner_id)
    return render_template('core/machines.html', machines=machines)


@bp.get('/models')
def models():
    type_id, owner_id = map(int, request.args.get('machines').split('_'))
    models = (Machine.select(Machine.id, Machine.model)
              .where((Machine.type_id == type_id) & (Machine.owner == owner_id)))
    return render_template('core/models.html', models=models)


@bp.get('/add_owner')
def add_owner():
    return render_template('core/add_owner.html')


# @bp.post('/new_owner')
# def new_owner():
#     form = request.form
#     title = form['add_owner']
#     Owner.create(title=title)
#     flash('Поставщик успешно создан')
#     return redirect(url_for('core.add_owner'))


@bp.post('/new_owner')
def new_owner():
    form = OwnerForm(request.form)
    title = form['owner'].data
    if not form.validate():
        return redirect(url_for('core.add_owner', result=0))
    else:
        Owner.create(title=title)
        return redirect(url_for('core.add_owner', result=1))
