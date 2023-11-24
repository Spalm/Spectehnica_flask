from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length


class AddTehniks(Form):
    model = StringField('модель')
    type = SelectField('тип', choices=['экскаватор-погрузчик', 'мини-погрузчик', 'мини-экскаватор', 'колесный экскаватор'])
    number = StringField('гос номер')
    owner = StringField('поставщик')
    user = SelectField('машинист', choices=['Сергей', 'Иван', 'Петр', 'Николай'])


