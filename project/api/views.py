# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, current_app)

from ..extensions import manager
# from ..models import MyModel


def initialize_api():
    # List all Flask-Restless APIs here
    # model_api = manager.create_api(MyModel, methods=['GET'])
    pass


api = Blueprint('api', __name__, url_prefix='/api')
