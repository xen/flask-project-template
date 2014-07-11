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


@manager.option('-s', '--source', dest='source', default='data/serialized_dump.txt', required=False, help='Source file')
def initdata(source='data/serialized_dump.txt'):
    print("Start importing data")
    with open(source, 'rb') as f:
        data = json.loads(f.readline())
    for model_data in data:
        try:
            restored = loads(model_data, db.metadata, db.session)
        except AttributeError, e:
            print('Table does not exist: {}'.format(e))
            continue
        if restored:
            print('Importing {} table...'.format(restored[0].__table__.name))
        for item in restored:
            db.session.merge(item)

        db.session.commit()

    seq_tables = []  # #List tables that need to have their sequences dropped here (postgresql only)
    for table_name in seq_tables:
        try:
            db.engine.execute("SELECT setval('{}_id_seq', (SELECT MAX(id) FROM {})+1);".format(table_name, table_name))
        except OperationalError:
            print('sequence bump for {} failed: not using PostgreSQL?'.format(table_name))
    print('Done')


@manager.option('-d', '--destination', dest='destination', default=None, required=True, help='Output file')
def dump_db(destination):
    dump_models = []  # #List your models here
    serialized = list()
    for model in dump_models:
        print('Dumping {}'.format(model))
        serialized.append(unicode(dumps(db.session.query(model).all()), errors='ignore'))
    with open(destination, 'w') as f:
        f.writelines(json.dumps(serialized))
    print 'Done.'



manager.add_option('-c', '--config', dest="config", required=False,
    help="config file")

if __name__ == "__main__":
    manager.run()
