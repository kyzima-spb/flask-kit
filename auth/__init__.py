# coding: utf-8

from flask import Blueprint


auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/')


from .models import User, Role
# from .views import *
