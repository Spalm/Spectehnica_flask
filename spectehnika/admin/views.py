from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.forms import LoginForm
from auth.models import Machine, User, Owner, MachineTypes
from core.forms import ReportForm, DataForm

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.get('/administration')
@login_required
def administration():
    report_form = ReportForm()
    owners = Owner.select(Owner.id, Owner.title)
    owners_choices = [(owner.id, owner.title) for owner in owners]
    owners_choices.insert(0, (0, 'Все поставщики'))
    report_form.owner.choices = owners_choices

    data_form = DataForm()
    context = {
        'report_form': report_form,
        'data_form': data_form,
    }
    return render_template('admin/administration.html', **context)


@bp.get('/owners')
def owners():
    owner_id = int(request.args.get('owner'))
    machines = Machine.select(Machine.type.distinct(), Machine.owner).join(MachineTypes)
    if owner_id:
        machines = machines.where(Machine.owner_id == owner_id)
    return render_template('core/machines.html', machines=machines)


@bp.get('/models')
def models():
    type_id, owner_id = map(int, request.args.get('machines').split('_'))
    models = (Machine.select(Machine.id, Machine.model)
              .where((Machine.type_id == type_id) & (Machine.owner == owner_id)))
    return render_template('core/models.html', models=models)


