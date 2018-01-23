# coding: utf-8

"""
    ext
    ~~~

    Good place for pluggable extensions.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

from flask_pony import Pony
from flask_security import Security, PonyUserDatastore
from flask_assets import Environment
from flask_gravatar import Gravatar
from flask_debugtoolbar import DebugToolbarExtension
# from flask.ext.restplus import Api


def security_factory(app):
    from auth.models import User, Role
    user_datastore = PonyUserDatastore(pony.db, User, Role)
    return Security(app, user_datastore)


pony = Pony()
security = security_factory
assets = Environment()
gravatar = Gravatar(size=50)
toolbar = DebugToolbarExtension()
# api = Api(default='api')
