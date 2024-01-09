from functools import cache

from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length

from auth.models import User, Role


@cache
def get_roles():
    roles = Role.select(Role.id, Role.title)
    return [(role.id, role.title) for role in roles]


class Employee(Form):
    name = StringField('имя')
    role = SelectField('должность')
    email = EmailField('почта', validators=[InputRequired('Введите email')])
    password = PasswordField('пароль', validators=[InputRequired('Введите пароль'),
                                                   Length(min=4, max=100)])

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        self.role.choices = get_roles()

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        user = User.get_or_none(email=self.email.data)
        if user is not None:
            self.email.errors.append('Пользователь с такой почтой уже есть')
            return False
        return True


