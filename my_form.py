from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class MyForm(FlaskForm):

    email = EmailField(label="email", validators=[DataRequired(), Email()])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Login")
