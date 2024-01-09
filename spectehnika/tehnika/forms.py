from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length


from auth.models import MachineTypes, Machine, User, Owner


class AddTehniks(Form):
    model = StringField('модель')
    type = SelectField('тип')
    number = StringField('гос номер')
    owner = SelectField('поставщик')
    user = SelectField('машинист')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        types = MachineTypes.select(MachineTypes.id, MachineTypes.title)
        types_choices = [(type_.id, type_.title) for type_ in types]
        self.type.choices = types_choices

        users = User.select(User.id, User.name)
        users_choice = [(user.id, user.name) for user in users]
        self.user.choices = users_choice

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



class AddType(Form):
    title = StringField('тип техники')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        types = MachineTypes.select(MachineTypes.id, MachineTypes.title)
        types_choices = [(type_.id, type_.title) for type_ in types]
        self.title.choices = types_choices

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        type_ = MachineTypes.get_or_none(title=self.title.data)
        if type_ is None:
            return True
        else:
            self.title.errors.append('Такой тип уже есть')
            return False
