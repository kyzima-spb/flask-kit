# coding: utf-8

"""
    settings
    ~~~~~~~~

    Global settings for project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "MY_VERY_SECRET_KEY"
    PONY = {
        'provider': 'sqlite',
        'dbname': '/tmp/db.sqlite'
    }
    CSRF_ENABLED = True
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

    BLUEPRINTS = [
        'auth.auth'
    ]

    EXTENSIONS = [
        'ext.pony',
        'ext.security',
        'ext.assets',
        'ext.gravatar',
        'ext.toolbar',
        # If you want Flask-RESTPlus out of the box
        # 'ext.api',
    ]

    CONTEXT_PROCESSORS = [
    ]

    CSS_BASE_BUNDLE = [
        'css/reset.css',
        'css/typo.css',
        'css/style.css',
        'css/page.css',
        'css/forms.css',
    ]

    JS_BASE_BUNDLE = [
    ]


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    PONY = {
        'provider': 'sqlite',
        'dbname': '/tmp/db_dev.sqlite'
    }


class TestingConfig(BaseConfig):
    TESTING = True
    PONY = {}
