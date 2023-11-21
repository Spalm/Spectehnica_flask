from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.forms import LoginForm
from auth.models import User, Owner
from core.forms import ReportForm, DataForm, AddSubleaseMachine

from auth.models import Machine

bp = Blueprint('core', __name__, url_prefix='/core')


@bp.get('/main')
def main():
    report_form = ReportForm()
    owners = Owner.select(Owner.id, Owner.title)
    owners_choices = [(owner.id, owner.title) for owner in owners]
    owners_choices.insert(0, (0, 'Все поставщики'))
    report_form.owner.choices = owners_choices

    models = Machine.select(Machine.model)

    data_form = DataForm()
    add_sublease = AddSubleaseMachine()
    context = {
        'report_form': report_form,
        'data_form': data_form,
        'add_sublease': add_sublease,
    }
    return render_template('core/main.html', **context)


@bp.get('/owners')
def owners():
    owner_id = int(request.args.get('owner'))
    machines = Machine.select(Machine.id, Machine.model)
    if owner_id:
        machines = machines.where(Machine.owner_id == owner_id)
    return render_template('core/machines.html', machines=machines)


@bp.get('test/<string:id>')
def test(id):
    return f'Запрос по маршруту /test/{id}'


