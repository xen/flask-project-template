import re
from flask.ext.wtf import Form
from flask.ext.babel import lazy_gettext

from wtforms.fields import TextField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import url, length, regexp, optional


class SettingsForm(Form):
    """docstring for SettingsForm"""

    ui_lang = SelectField(
        label=lazy_gettext("Primary site language"),
        description=lazy_gettext("Site will try to show UI labels using this " +
            "language. User data will be shown in original languages."),
    )
    url = URLField(
        label=lazy_gettext("Personal site URL"),
        description=lazy_gettext("If you have personal site and want to share " +
            "with other people, please fill this field"),
        validators=[optional(), url(message=lazy_gettext("Invalid URL."))])
    username = TextField(
        label=lazy_gettext("Public profile address"),
        description=lazy_gettext("Will be part of your public profile URL. Can " +
            "be from 2 up to 40 characters length, can start start from [a-z] " +
            "and contains only latin [0-9a-zA-Z] chars."),
        validators=[
            length(2, 40, message=lazy_gettext("Field must be between 2 and 40" +
            " characters long.")),
            regexp(r"[a-zA-Z]{1}[0-9a-zA-Z]*",
                re.IGNORECASE,
                message=lazy_gettext("Username should start from [a-z] and " +
                    "contains only latin [0-9a-zA-Z] chars"))
        ]
    )
