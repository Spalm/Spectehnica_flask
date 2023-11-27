from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length

from auth.models import MachineTypes


class AddTehniks(Form):
    model = StringField('модель')
    type = SelectField('тип')
    number = StringField('гос номер')
    owner = SelectField('поставщик')
    user = SelectField('машинист')


class AddType(Form):
    title = StringField('тип техники')

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        type_ = MachineTypes.get_or_none(title=self.title.data)
        if type_ is None:
            return True
        else:
            self.title.errors.append('Такой поставщик уже есть')
            return False

