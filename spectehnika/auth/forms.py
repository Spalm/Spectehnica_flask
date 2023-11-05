from wtforms import Form, EmailField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    email = EmailField('Email', [validators.Email()])
    password = PasswordField('Пароль',  validators=[DataRequired(), Length(min=4, max=100)])
    # submit = SubmitField("Войти")
