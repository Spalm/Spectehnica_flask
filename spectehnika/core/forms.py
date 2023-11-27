from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField

from auth.models import Machine, Owner


class ReportForm(Form):
    date1 = DateField('начальная дата')
    date2 = DateField('конечная дата')
    owner = SelectField('поставщик')
    machine = SelectField('тип техник')
    model = SelectField('модель')


class DataForm(Form):
    date = DateField('дата')
    address = StringField('адрес')
    owner = SelectField('поставщик')
    type = SelectField('тип')
    model = SelectField('модель')
    hours = IntegerField('часы')
    cost = IntegerField('закупка')
    sell = IntegerField('продажа')



