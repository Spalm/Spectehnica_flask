from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.forms import LoginForm
from auth.models import User, Owner, MachineTypes
from core.forms import ReportForm, DataForm

from auth.models import Machine
from tehnika.forms import AddTehniks

bp = Blueprint('core', __name__, url_prefix='/core')


@bp.get('/main')
def main():
    form = AddTehniks()
    data_form = DataForm()
    report_form = ReportForm()
    owners = Owner.select(Owner.id, Owner.title)
    owners_choices = [(owner.id, owner.title) for owner in owners]
    report_form.owner.choices = owners_choices
    form.owner.choices = owners_choices

    tehniks = Machine.select(Machine.model, Machine.user, Machine.number).join(User).where(Machine.owner == 1)

    users = User.select(User.id, User.name)
    users_choise = [(user.id, user.name) for user in users]
    form.user.choices = users_choise

    types = MachineTypes.select(MachineTypes.id, MachineTypes.title)
    types_choises = [(type_.id, type_.title) for type_ in types]
    form.type.choices = types_choises


    context = {
        'report_form': report_form,
        'data_form': data_form,
        'tehniks': tehniks,
        'form': form
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


@bp.post('/new_owner')
def new_owner():
    form = request.form
    title = form['add_owner']
    Owner.get_or_create(title=title)
    return render_template('core/main.html')
