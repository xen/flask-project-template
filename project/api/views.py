# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, current_app)

from ..extensions import manager
# from ..models import MyModel


def initialize_api(app):
    with app.app_context():
        # List all Flask-Restless APIs here
        # model_api = manager.create_api(MyModel, methods=['GET'],
        #                                app=app,
        #                                url_prefix='/api')
        pass


api = Blueprint('api', __name__)
