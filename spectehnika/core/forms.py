from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, FormField, validators

from auth.models import Machine, Owner, MachineTypes


class ReportRowForm(Form):
    date1 = DateField('дата')
    date2 = DateField('конечная дата')
    owner = SelectField('поставщик')
    machine = SelectField('тип техник')
    model = SelectField('модель')
    hours = StringField('часы')
    address = StringField('адрес')
    cost = IntegerField('закупка')
    price = IntegerField('продажа')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        owners = Owner.select(Owner.id, Owner.title)
        owner_choices = [(owner.id, owner.title) for owner in owners]
        owner_choices.insert(0, (0, 'Не выбрано'))
        self.owner.choices = owner_choices


class ReportForm(Form):
    row1 = FormField(ReportRowForm)
    row2 = FormField(ReportRowForm)
    row3 = FormField(ReportRowForm)
    row4 = FormField(ReportRowForm)
    row5 = FormField(ReportRowForm)


class GetReportForm(Form):
    date1 = DateField('дата', validators=[validators.InputRequired()])
    date2 = DateField('конечная дата', validators=[validators.InputRequired()])
    owner = SelectField('поставщик')
    machine = SelectField('тип техник')
    model = SelectField('модель')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)

        owners = Owner.select(Owner.id, Owner.title)
        owner_choices = [(0, 'Все')]
        owner_choices.extend([(owner.id, owner.title) for owner in owners])
        self.owner.choices = owner_choices

        machine_types = MachineTypes.select(MachineTypes.id, MachineTypes.title)
        machine_types_choices = [(0, 'Все')]
        machine_types_choices.extend([(type_.id, type_.title) for type_ in machine_types])
        self.machine.choices = machine_types_choices

        machines = Machine.select(Machine.id, Machine.model)
        machine_choices = [(0, 'Все')]
        machine_choices.extend([(machine.id, machine.model) for machine in machines])
        self.model.choices = machine_choices


class OwnerForm(Form):
    owner = StringField('наименование компании')

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        owner = Owner.get_or_none(title=self.owner.data)
        if owner is None:
            return True
        else:
            self.owner.errors.append('Такая компания уже есть')
            return False


class AddSublease(Form):
    model = StringField('модель')
    type = SelectField('тип')
    number = StringField('гос номер')
    owner = SelectField('поставщик')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        types = MachineTypes.select(MachineTypes.id, MachineTypes.title)
        types_choices = [(type_.id, type_.title) for type_ in types]
        self.type.choices = types_choices

        owners = Owner.select(Owner.id, Owner.title)
        owner_choices = [(owner.id, owner.title) for owner in owners]
        self.owner.choices = owner_choices

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        machine = Machine.get_or_none(number=self.number.data)
        if machine is not None:
            self.number.errors.append('Машина с таким номером уже есть')
            return False
        return True

