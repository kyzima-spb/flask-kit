# coding: utf-8

"""
    base.forms
    ~~~~~~~~~~

    The most common forms for the whole project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired


class LoginForm(Form):
    email = StringField('Login', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
