from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):

    email = EmailField(label="email", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="Login")
