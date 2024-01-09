from flask import Flask, render_template, redirect, url_for, request, make_response, Blueprint, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from auth.models import Machine, User, MachineTypes, Owner, Report

bp = Blueprint('rep', __name__, url_prefix='/rep')


@bp.get('report/<int:id>')
def report_row(id: int):
    context = {
        'row': Report.get_by_id(id)
    }
    return render_template('report/report_row.html', **context)


@bp.get('report/<int:id>/edit')
def get_edit_report(id: int):
    context = {
        'row': Report.get_by_id(id)
    }
    return render_template('report/edit_report.html', **context)


@bp.put('report/<int:id>')
def put_edit_report(id: int):
    report = Report.get_by_id(id)
    report.hours = request.form['hours']
    report.cost = request.form['cost']
    report.price = request.form['price']
    report.save()

    context = {
        'row': Report.get_by_id(id)
    }
    return render_template('report/report_row.html', **context)


@bp.delete('del_report/<int:id>')
def del_report(id: int):
    Report.delete_by_id(id)
    return ''
