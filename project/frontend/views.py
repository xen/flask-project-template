# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, g, request, url_for,
    current_app, send_from_directory, json, redirect, make_response, abort)

from flask.ext.login import login_required

from ..extensions import pages, csrf
from ..tasks import do_some_stuff

frontend = Blueprint('frontend', __name__, template_folder="templates")


@frontend.route('/')
def index():
    # Run background task inside of view
    do_some_stuff.delay()
    return render_template('frontend/index.html')


@frontend.route('/docs/', defaults={'path': 'index'})
@frontend.route('/docs/<path:path>/', endpoint='page')
def page(path):
    # Documentation views
    _page = pages.get_or_404(path)
    return render_template('page.html', page=_page)


@frontend.route('/robots.txt')
def static_from_root():
    # Static items
    return send_from_directory(current_app.static_folder, request.path[1:])


@frontend.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.png')

