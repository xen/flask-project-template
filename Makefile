all: setup

venv/bin/activate:
	virtualenv-2.7 venv

run: venv/bin/activate requirements.txt
	. venv/bin/activate; python manage.py runserver

setup: venv/bin/activate requirements.txt
	. venv/bin/activate; pip install -Ur requirements.txt
	cd static && bower install

init: venv/bin/activate requirements.txt
	. venv/bin/activate; python manage.py db upgrade 

babel: venv/bin/activate
	. venv/bin/activate; pybabel extract -F babel.cfg -o project/translations/messages.pot project

# lazy babel scan
lazybabel: venv/bin/activate
	. venv/bin/activate; pybabel extract -F babel.cfg -k lazy_gettext -o project/translations/messages.pot project

# run: 
# $ LANG=en make addlang
addlang: venv/bin/activate
	. venv/bin/activate; pybabel init -i project/translations/messages.pot -d project/translations -l $(LANG)

updlang: venv/bin/activate
	. venv/bin/activate; pybabel update -i project/translations/messages.pot -d project/translations
