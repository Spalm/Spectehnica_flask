from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length


class AddTehniks(Form):
    model = StringField('модель')
    type = SelectField('тип')
    number = StringField('гос номер')
    owner = StringField('поставщик')
    user = SelectField('машинист')


