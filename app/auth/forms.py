import wtforms
from wtforms.validators import Required, Email, Length, EqualTo
from flask_wtf import FlaskForm

from ..models import User

class RegistrationUser(FlaskForm):
    email = wtforms.StringField('Email',validators=[Required(),
                            Length(1,64),Email()])
    username = wtforms.StringField('Username',validators=[Required(),
                            Length(1,64),])
    password = wtforms.PasswordField('Password',validators=[Required(),
                            EqualTo('password2',message='Password must match.')])
    password2 = wtforms.PasswordField('Confirm password', validators=[Required()])
    submit = wtforms.SubmitField('Click me')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise wtforms.ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise wtforms.ValidationError('Username already in user')

class LoginForm(FlaskForm):
    email = wtforms.StringField('Email', validators=[wtforms.validators.Required(),
                            wtforms.validators.Length(1,64), wtforms.validators.Email()])
    password = wtforms.PasswordField('Password', validators=[wtforms.validators.Required()])
    submit = wtforms.SubmitField('Log in')