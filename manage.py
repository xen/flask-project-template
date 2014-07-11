#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import json

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from project import create_app
from project.extensions import db

from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.serializer import dumps, loads

manager = Manager(create_app)
# Add Flask-Migrate commands under `db` prefix, for example:
# $ python manage.py db init
#
# $ python manage.py db migrate
#

manager.add_command('db', MigrateCommand)


@manager.command
def init():
    """Run in local machine."""
    syncdb()


@manager.command
def syncdb():
    """Init/reset database."""
    db.drop_all()
    db.create_all()


manager.add_option('-c', '--config', dest="config", required=False,
    help="config file")

if __name__ == "__main__":
    manager.run()
