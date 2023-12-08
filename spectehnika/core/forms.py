from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField

from auth.models import Machine, Owner


class ReportForm(Form):
    date1 = DateField('начальная дата')
    date2 = DateField('конечная дата')
    owner = SelectField('поставщик')
    machine = SelectField('тип техник')
    model = SelectField('модель')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        owners = Owner.select(Owner.id, Owner.title)
        owner_choices = [(owner.id, owner.title) for owner in owners]
        self.owner.choices = owner_choices


class DataForm(Form):
    date = DateField('дата')
    address = StringField('адрес')
    owner = SelectField('поставщик')
    type = SelectField('тип')
    model = SelectField('модель')
    hours = IntegerField('часы')
    cost = IntegerField('закупка')
    sell = IntegerField('продажа')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        owners = Owner.select(Owner.id, Owner.title)
        owner_choices = [(owner.id, owner.title) for owner in owners]
        self.owner.choices = owner_choices


class OwnerForm(Form):
    owner = StringField('наименование компании')

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        owner = Owner.get_or_none(title=self.owner.data)
        if owner is not None:
            return True
        else:
            self.owner.errors.append('Такая компания уже есть')
            return False




