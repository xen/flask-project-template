# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, g, request, url_for,
    current_app, send_from_directory, json, redirect, make_response, abort)

from flask.ext.login import login_required

from ..extensions import pages, csrf
from ..models import Country, UserCountry, User

frontend = Blueprint('frontend', __name__, template_folder="templates")


@frontend.before_request
def before_request():
    # Add to global vars list of the projects owned by current user
    if g.user:
        pass
        # g.my_countries = Project.query.filter_by(login=g.user.login).all()


@frontend.route('/')
def index():
    cdata = {
        country.iso.lower(): country.name
        for country in Country.query.order_by("name asc").all()
    }
    country = request.headers.get('CF-IPCountry') or 'ua'
    return render_template('frontend/splash.html', cdata=cdata,
        from_country=country, country_list=json.dumps(cdata))


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


@csrf.exempt
@frontend.route('/search')
def search():
    if request.args.get('from') and request.args.get('to'):
        return redirect(url_for('country.visa', cfrom=request.args.get('from'),
            cto=request.args.get('to')))
    elif request.args.get('from'):
        return redirect(url_for('country.visa_list',
            code=request.args.get('from')))
    elif request.args.get('to'):
        return redirect(url_for('country.info', code=request.args.get('to')))

    return redirect(url_for('frontend.index'))


@frontend.route('/user/<string:username>')
def user_profile(username):
    user_profile = User.query.filter_by(username=username).first_or_404()
    user_country = UserCountry.query.filter_by(user=user_profile).all()
    return render_template('frontend/user_profile.html',
        user_profile=user_profile, user_country=user_country)


@frontend.route('/my-list')
@login_required
def mylist():
    countries = Country.query.order_by("name asc").all()
    return render_template('country/all.html', countries=countries)
