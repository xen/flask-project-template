# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, g, request, url_for,
    current_app, send_from_directory, json, redirect, make_response, abort)

from flask.ext.login import login_required

from ..extensions import pages, csrf
from ..models import User

frontend = Blueprint('frontend', __name__, template_folder="templates")


@frontend.before_request
def before_request():
    # Add to global vars list of the projects owned by current user
    if g.user:
        pass
        # g.my_countries = Project.query.filter_by(login=g.user.login).all()


@frontend.route('/')
def index():
    return render_template('frontend/splash.html')


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


@frontend.route('/user/<string:username>')
def user_profile(username):
    user_profile = User.query.filter_by(username=username).first_or_404()
    return render_template('frontend/user_profile.html',
        user_profile=user_profile)


