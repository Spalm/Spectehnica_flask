from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.models import Machine, User, Owner, MachineTypes, Report
from core.forms import ReportForm, ReportRowForm, GetReportForm

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.get('/administration')
@login_required
def administration():
    report_form = GetReportForm()
    context = {
        'report_form': report_form,
        'current_user': current_user
    }
    return render_template('admin/administration.html', **context)


@bp.get('/owners')
def owners():
    owner_id = int(request.args.get('owner'))
    machines = Machine.select(Machine.type.distinct(), Machine.owner).join(MachineTypes)
    if owner_id != 0:
        machines = machines.where(Machine.owner_id == owner_id)
    additional_choices = [
        (0, 'Все')
    ]
    context = {
        'machines': machines,
        'additional_choices': additional_choices,
    }
    return render_template('core/machines.html', **context)


@bp.get('/models')
def models():
    type_id, owner_id = map(int, request.args.get('machine').split('_'))
    models = Machine.select(Machine.id, Machine.model)
    if type_id != 0:
        models = models.where((Machine.type_id == type_id) & (Machine.owner == owner_id))

    additional_choices = [
        (0, 'Все')
    ]
    context = {
        'models': models,
        'additional_choices': additional_choices,
    }
    return render_template('core/models.html', **context)


@bp.post('report')
def get_report():
    form = GetReportForm(request.form)
    start_date = form.date1.data
    end_date = form.date2.data
    owner = int(form.owner.data)
    model = int(form.model.data)
    type = int(form.machine.data.split('_')[0])

    filters = Report.date.between(start_date, end_date)
    if owner:
        filters &= Report.owner == owner
    if type:
        filters &= Report.type == type
    if model:
        filters &= Report.model == model

    reports = (Report
               .select()
               .join(Owner)
               .where(filters))

    context = {
        'reports': reports,
        'start_date': start_date.strftime('%d.%m.%Y'),
        'end_date': end_date.strftime('%d.%m.%Y')
    }

    return render_template('report/report.html', **context)
