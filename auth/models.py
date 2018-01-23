# coding: utf-8

from flask_security import UserMixin, RoleMixin
from pony.orm import Required, Optional, Set

from ext import pony

db = pony.db


class User(db.Entity, UserMixin):
    email = Required(str, 255)
    password = Required(str, 255)
    name = Optional(str, 255)
    active = Required(bool, default=True)
    roles = Set('Role')


class Role(db.Entity, RoleMixin):
    name = Required(str, 80, unique=True)
    description = Required(str, 255)
    users = Set('User')
