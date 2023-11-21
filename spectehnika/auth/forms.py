from wtforms import Form, EmailField, PasswordField, validators
from wtforms.validators import InputRequired, Length

from auth.models import User


class LoginForm(Form):
    email = EmailField('Email', validators=[
        InputRequired('Введите email')
    ]
                       )
    password = PasswordField('Пароль', validators=[
        InputRequired('Введите пароль'),
        Length(min=4, max=100)
    ]
                             )

    def validate(self, extra_validators=None) -> bool:
        if not super().validate(extra_validators):
            return False

        user = User.get_or_none(email=self.email.data, password=self.password.data)
        if user is None:
            self.password.errors.append('Неверный email или пароль')
            return False

        return True
