from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length

from auth.models import User


class Employee(Form):
    name = StringField('имя')
    role = StringField('должность')
    email = EmailField('почта', validators=[InputRequired('Введите email')])
    password = PasswordField('пароль', validators=[InputRequired('Введите пароль'),
                                                   Length(min=4, max=100)])

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        user = User.get_or_none(email=self.email.data)
        if user is None:
            return True
        else:
            self.errors.errors.append('Пользователь с такой почтой уже ест')
            return False


