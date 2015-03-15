# -*- coding: utf-8 -*-

from flask.ext.mail import Mail
mail = Mail()

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_flatpages import FlatPages
pages = FlatPages()

import flask.ext.restless
manager = flask.ext.restless.APIManager()

from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

from flask.ext.babel import Babel
babel = Babel()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.wtf.csrf import CsrfProtect
csrf = CsrfProtect()

from flask.ext.cache import Cache
cache = Cache()

from celery import Celery
celery = Celery()
