# -*- coding: utf-8 -*-
from hashlib import md5
from ..extensions import db
from flask.ext.login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    # tables name convention is contradictory topic, usually I'm against plural forms
    # when name tables, but user is reserved word in post databases,
    # so this is only case when it is allowed to use plural in my teams.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200), default='')
    name = db.Column(db.String(100))
    email = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)
    ui_lang = db.Column(db.String(2), default='en')
    url = db.Column(db.String(200))

    def gavatar(self, size=14):
        if self.email:
            return 'http://www.gravatar.com/avatar/{hashd}?d=mm&s={size}'.format(
                hashd=md5(self.email).hexdigest(), size=str(size))
        else:
            return None

    def is_active(self):
        return self.active

    def get_access_token(self, provider, param_name='access_token'):
        """ Method can be used for social network API access.

            >>> import requests
            >>> user = User.query.one()
            >>> r = requests.get('https://api.github.com/user',
            ...    params={'access_token': user.get_access_token('github')})
            >>> r.json()['html_url']
            u'https://github.com/xen'

        """
        # provider should be from social providers list, for example 'github'
        s = self.social_auth.filter_by(provider=provider).one()
        return s.extra_data.get(param_name, None)
