# Flask project template

`Flask project template` contains working example of Flask project with features:

- Ready to ship Flask project template
- **Database migrations** out-of-the-box migrations (uses Alembic)
- Simple setup `make setup & make run` which make local virtualenv isolated environment and doesn't trash your system python.
- Contains `Dockerfile` that allow to setup full linux environment on any host OS supported by Docker
- Static files managed by `bower`. By default templates uses `Bootstrap` but doesn't force you to use this UI framework.
- Have working example of GitHub **OAuth authorization**, you only need to provide your own security and secret key (will work with example keys only on `localhost:5000`). Allow user login/logout 
- **i18n** via integrated Babel support and special support targets for `make`
- User settings page with ability to switch site language
- `Flask-FlatPages` support to simplify static pages management
- Builtin `Flask-Script` support with shell
- **Fixtures** sump/restore support

## How to start

Follow this steps:

- [Fork project](https://github.com/xen/flask-project-template/fork)
- Download/clone your own copy
- Run `make setup`
- Run `make init` to create sqlite database file
- `make run`, you have working site
- Open browser http://127.0.0.1:5000/
- Customize project files and have fun

## Requirements

You can simple run project inside of Docker container or on your prefered environment. If you want to run on your own environment you need:
- Recent python supported version with sqlite library (usually it is included) 
- Working `virtualenv-2.7` command, name can vary, so you can change it inside `Makefile`
- `make`
- [`bower`](http://bower.io/), if you already have `node.js` with `npm` then run this command:
```sh
npm install -g bower
```

## Included modules support

- [`Flask`](http://flask.pocoo.org/) & [`Werkzeug`](http://werkzeug.pocoo.org/) — base for everything
- [`Babel`](http://babel.pocoo.org/) & [`Flask-Babel`](https://pythonhosted.org/Flask-Babel/) — i18n support
- [`Flask-FlatPages`](https://pythonhosted.org/Flask-FlatPages/) with [`Markdown`](https://pythonhosted.org/Markdown/) — to maintain auxiliary pages (About, Contacts, etc)
- [`Flask-Script`](http://flask-script.readthedocs.org/) — simplify management tasks
- [`Flask-WTF`](https://flask-wtf.readthedocs.org/) — form validation
- [`flask-restless`](http://flask-restless.readthedocs.org/) — various API
- [`Flask-SQLAlchemy`](https://pythonhosted.org/Flask-SQLAlchemy/) — database ORM layer
- [`flask-migrate`](http://flask-migrate.readthedocs.org/) — database schema migration support
- [`python_social_auth`](https://github.com/omab/python-social-auth) & [`Flask-Login`](https://flask-login.readthedocs.org/) — social networks login


## `make` commands overview

There is several usefull targets in `Makefile`:

- `setup` — will make local virtualenv environment and install all dependencies including JavaScript libraries in `static` folder
- `run` — local run server in DEBUG mode
- `init` — synchronize database scheme and apply migrations. This target should be idempotent (if you run in several times you will get the same results in the end), but if you work with several database at once sometimes in need manual tuning.
- `babel` and `lazybabel` — generate `project/translations/messages.pot` file with different strategy. 
- `addlang` — add new language translation with code taken from shell variable `LANG`. Simple usage example `$ LANG=en make addlang`
- `updlang` — update language files in language folders made by `addlang` command. 

Translation workflow in nutshell:

- Edit templates and py files
- Run `lazybabel` if new translations strings were added or modified
- Run `updlang` to apply master `.pot` files changes to `.po` language files
- Run `addlang` if you need to support another language
- Update `project/config.py` `LANGUAGES` dict to allow users see new translations in Settings page
- Use [Poedit](http://poedit.net/) to translate strings

## `manage.py` command overview

TBD

## Project structure

TBD

