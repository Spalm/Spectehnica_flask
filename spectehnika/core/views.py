import datetime

from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint, flash
from flask_login import login_required, current_user

from auth.models import User, Owner, Machine, Report, MachineTypes
from core.forms import ReportForm, OwnerForm, GetReportForm, AddSublease
from tehnika.forms import AddTehniks

bp = Blueprint('core', __name__, url_prefix='/core')


@bp.get('/main')
@login_required
def main():
    get_report = GetReportForm()
    form = AddSublease()
    form_owner = OwnerForm()
    report_form = ReportForm()
    tehniks = Machine.select(Machine.model, Machine.user, Machine.number).join(User).where(Machine.owner == 1)

    context = {
        'form_owner': form_owner,
        'get_report': get_report,
        'report_form': report_form,
        'tehniks': tehniks,
        'form': form,
        'current_user': current_user
    }
    return render_template('core/main.html', **context)


@bp.get('/owners')
def owners():
    keys = [arg for arg in request.args if arg.endswith('-owner')]
    if len(keys) != 1:
        raise ValueError('Multiple or none "-owner" args')

    owner_id = int(request.args[keys[0]])
    machines = Machine.select(Machine.type.distinct(), Machine.owner).join(MachineTypes)
    if owner_id:
        machines = machines.where(Machine.owner_id == owner_id)
    return render_template('core/machines.html', machines=machines)


@bp.get('/models')
def models():
    keys = [arg for arg in request.args if arg.endswith('-machine')]
    if len(keys) != 1:
        raise ValueError('Multiple or none "-owner" args')
    result = request.args[keys[0]]
    type_id, owner_id = map(int, result.split('_'))
    models = (Machine.select(Machine.id, Machine.model)
              .where((Machine.type_id == type_id) & (Machine.owner == owner_id)))
    return render_template('core/models.html', models=models)


# @bp.get('/add_owner')
# def add_owner():
#     form_owner = OwnerForm()
#     return render_template('core/add_owner.html', form_owner=form_owner)


@bp.post('/new_owner')
def new_owner():
    form = OwnerForm(request.form)
    title = form['owner'].data
    if not form.validate():
        form.owner.data = ''
        return render_template('core/add_owner.html', form=form)
    else:
        form.owner.data = ''
        Owner.create(title=title)
        return render_template('core/add_owner.html', show_success_message=1, form=form)


# @bp.get('/add_sublease')
# def add_sublease():
#     form = AddTehniks()
#     return render_template('core/sublease_form.html', form=form)
#

@bp.post('/new_sublease')
def new_sublease():
    form = AddSublease(request.form)
    if not form.validate():
        form.model.data = ''
        form.number.data = ''
        return render_template('core/sublease_form.html', form=form)

    owner = int(form.owner.data)
    model = form.model.data
    number = form.number.data
    type_ = int(form.type.data)

    form.model.data = ''
    form.number.data = ''
    Machine.create(owner=owner, model=model, number=number, type=type_, user=None)
    return render_template('core/sublease_form.html', show_success_message=1, form=form)


@bp.post('create_report')
def create_report():
    form = ReportForm(request.form)
    for row in form:
        if any(field is None for field in row.data.values()):
            continue
        date = row.data["date1"]
        end_date = row.data["date2"]

        days = 0
        day = row.data["date1"]
        while day <= end_date:
            day += datetime.timedelta(days=1)
            days += 1

        hours = int(row.data["hours"]) / days

        while date <= end_date:
            type_ = row.data["machine"].split('_')[0]
            Report.create(date=date, address=row.data["address"],
                          owner=row.data["owner"], type=type_,
                          model=row.data["model"], hours=hours,
                          cost=row.data["cost"], price=row.data["price"])
            date += datetime.timedelta(days=1)
    return redirect(url_for('core.main'))


