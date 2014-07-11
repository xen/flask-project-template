# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, request, current_app, g, flash, url_for
from flask.ext.login import login_required, logout_user
from flask.ext.babel import gettext as _
from .models import User
from ..extensions import db
from .forms import SettingsForm

auth = Blueprint('auth', __name__, url_prefix='/auth/', template_folder="templates")


@auth.route('login')
def login():
    next_url = request.args.get('next') or request.referrer or None
    return render_template('auth/index.html', next=next_url)


@auth.route('loggedin')
def loggedin():
    return redirect(request.args.get('next') or url_for('frontend.index'))


@auth.route('profile')
@login_required
def profile():
    return render_template('auth/profile.html')


@auth.route('set_lang')
@login_required
def set_lang():
    if request.args.get('lang') in current_app.config['LANGUAGES']:
        user = User.query.get_or_404(g.user.id)
        user.ui_lang = request.args.get('lang')
        db.session.add(user)
        db.session.commit()
    return redirect('/')


@auth.route('settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm(request.form, g.user)
    form.ui_lang.choices = current_app.config['LANGUAGES'].items()

    if form.validate_on_submit():
        form.populate_obj(g.user)
        db.session.add(g.user)
        db.session.commit()
        flash(_("Settings saved"))

    return render_template('auth/settings.html', languages=current_app.config['LANGUAGES'], form=form)


@auth.route('logout')
def logout():
    logout_user()
    return redirect('/')
