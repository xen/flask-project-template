# Flask project template

`Flask project template` contains working example of Flask project with features:

- Ready to ship Flask project template
- **Database migrations** out-of-the-box (uses Alembic)
- Simple setup `make setup && make run` which make local virtualenv isolated environment and doesn't trash your system python.
- Contains `Dockerfile` that allow to setup full linux environment on any host OS supported by Docker
- Static files managed by `bower`. By default templates uses `Bootstrap` but doesn't force you to use this UI framework.
- Have working example of GitHub **OAuth authorization**, you only need to provide your own security and secret key (will work with example keys only on `127.0.0.1:5000`). Allow user login/logout 
- **i18n** and **l10n** via integrated Babel support and `make` targets 
- User settings page with ability to switch site language
- `Flask-FlatPages` support to simplify static pages management
- Built In `Flask-Script` shell commands
- **Fixtures** dump/restore support
- Inegrated [Celery](http://celeryproject.org/) background tasks management
- Cache using [Flask-Cache](https://pythonhosted.org/Flask-Cache/)
- Logging with example how to make email notifications when something goes wrong on server

## How to start

There is two ways. First way is use [`cookiecutter`](https://github.com/audreyr/cookiecutter) template (it located in [different repository](https://github.com/xen/flask-ptc)):

    cookiecutter https://github.com/xen/flask-ptc.git

Second way is manually clone this repository and change it later by own. Project is ready to run (with some requrements). You need to clone and run:

    $ mkdir Project
    $ cd Project
    $ git clone git@github.com:xen/flask-project-template.git .
    $ make
    $ make run

Open http://127.0.0.1:5000/, customize project files and **have fun**.

If you have any ideas how to improve it [Fork project](https://github.com/xen/flask-project-template/fork) and send me pull request.

## Requirements

If you never worked with python projects then simpliest way is run project inside Docker. Follow instruction [how to install Docker in your OS](https://docs.docker.com/installation/).

If you familiar with web development then you need Python and Node.js:
- Recent Python supported version with sqlite library (usually it is included) 
- Working `virtualenv` command, name can vary, so you can change it inside `Makefile`
- `make`
- [`bower`](http://bower.io/), if you already have `node.js` with `npm` then run this command:
```sh
npm install -g bower
```

**Can I use Python 3?**

This Flask project template is Python 3 ready, but unfortunately some of Flask extensions or python modules can be incompatible with Python 3.x. If you are sure that you don't need one of them then try to use Python 3.x or PyPy.

## Included modules support

- [`Flask`](http://flask.pocoo.org/) & [`Werkzeug`](http://werkzeug.pocoo.org/) — base for everything.
- [`Babel`](http://babel.pocoo.org/) & [`Flask-Babel`](https://pythonhosted.org/Flask-Babel/) — i18n support.
- [`Flask-FlatPages`](https://pythonhosted.org/Flask-FlatPages/) with [`Markdown`](https://pythonhosted.org/Markdown/) — to maintain auxiliary pages (About, Contacts, etc).
- [`Flask-Script`](http://flask-script.readthedocs.org/) — simplify management tasks.
- [`Flask-WTF`](https://flask-wtf.readthedocs.org/) — form validation.
- [`flask-restless`](http://flask-restless.readthedocs.org/) — restfull API generator.
- [`Flask-SQLAlchemy`](https://pythonhosted.org/Flask-SQLAlchemy/) — database ORM layer build on top of SQLAlchemy, best python ORM with depth and flexibility.
- [`flask-migrate`](http://flask-migrate.readthedocs.org/) — database schema migration support.
- [`python_social_auth`](https://github.com/omab/python-social-auth) & [`Flask-Login`](https://flask-login.readthedocs.org/) — social networks login.
- [`Celery`](http://celeryproject.org/) — background and defered tasks broker.
- [`Flask-Cache`](https://pythonhosted.org/Flask-Cache/) — tiny cache extension. Since I found myself using cache in most projects added this package to the list.

## `make` commands overview

There is several useful targets in `Makefile`:

- `setup` — will make local virtualenv environment and install all dependencies including JavaScript libraries in `static` folder
- `run` — local run server in DEBUG mode
- `init` — synchronize database scheme and apply migrations. This target should be idempotent (if you run in several times you will get the same results in the end), but if you work with several database at once sometimes in need manual tuning.
- `babel` and `lazybabel` — generate `project/translations/messages.pot` file with different strategy. 
- `addlang` — add new language translation with code taken from shell variable `LANG`. Simple usage example `$ LANG=en make addlang`
- `updlang` — update language files in language folders made by `addlang` command.
- `celery` — run celery broker
- `dcelery` — run celery broker in debug state with code reload and verbose output. Sometimes require manual reloads, but more handy during development

Translation workflow in nutshell:

- Edit templates and py files
- Run `lazybabel` if new translations strings were added or modified
- Run `updlang` to apply master `.pot` files changes to `.po` language files
- Run `addlang` if you need to support another language
- Update `project/config.py` `LANGUAGES` dict to allow users see new translations in Settings page
- Use [Poedit](http://poedit.net/) to translate strings

## `manage.py` command overview

`Flask-Script` added flawor of Django `manage.py` to Flask development. Put your common management tasks inside this file. Migration commands already available with `db` prefix. For example how to make new migration and upgrade your database:

    $ python manage.py db migrate -m "new models"
    $ python manage.py db upgrade
    # don't forget to add new file under git control
    $ git add migrations/versions/*.py

By default `manage.py` already have this commands:

* `init` — recreate all tables in database. Usually you don't need to use this command since it will erase all your data, but on empty environment can be usefull on local enviroment.
* `dump` — make fixture and save all data contained in models defined in `dump_models` variable. 
* `restore` — restore fixtures from file created by `dump` command.

## Project structure

After you checkout this code you may need to rename folder `project` to something more relevant your needs. I prefer to have own name for each individual project. Next step to change all mentions of word `project` in your code. I don't added any code generators for this project since anyway make code reviews every time starting new Flask project by adding or removing extensions or some parts of the source code.

    .
    ├── Dockerfile

If you need run project inside `Docker`

    ├── Makefile
    ├── README.md
    ├── babel.cfg

Configuration for `Flask-Babel`, generally you don't need to edit this file unless you use different template system.

    ├── celery_run.py

To run Celery brocker use this file.

    ├── entry.py

To run Flask server use this file, it is already prepared for `uwsgi`, `mod_wsgi` or other wsgi webserver modules.

    ├── local.example.cfg

Rename this file to `local.cfg` and use on different versions on product, test and development environment.

    ├── manage.py

Use this file to register management commands. Alembic commands set already included with `db` prefix. 

    ├── migrations
    │   ├── README
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── ee69294e63e_init_state.py

Migrations folder contains all your database migrations. 

    ├── packages.txt

This file used by Docker and contains all Ubuntu packages that need to be installed on fresh Ubuntu server.

    ├── project

Your project code is here

    │   ├── __init__.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── views.py

Put here your your admin or API views created by `Flask-Admin` or `Flask-Restless`.

    │   ├── app.py

This cornerstone part of the project structure. But export only two functions `create_app` and `create_celery`. More info [inside file](https://github.com/xen/flask-project-template/blob/master/project/app.py). 

    │   ├── auth
    │   │   ├── __init__.py
    │   │   ├── forms.py
    │   │   ├── models.py
    │   │   ├── templates
    │   │   │   └── auth
    │   │   │       ├── index.html
    │   │   │       ├── macros.html
    │   │   │       ├── profile.html
    │   │   │       └── settings.html
    │   │   └── views.py

`project.auth` is working example of blueprint which show how to organize user authentication using different OAuth providers, such as Facebook, GitHub, Twitter, etc. [Full list of supported social backends](http://psa.matiasaguirre.net/docs/backends/index.html#social-backends) available in `python-social-auth` documentation page.

    │   ├── config.py

File contains default configuration for the project. My personal approach to have code that can run with defaults. When you don't need special Postgres or other database features on deployment environment for testing purpose enough to use SQLite, but set of projects that are database agnostic is very limited in real life. More about [configuration](#configuration) is separate chapter.

    │   ├── docs
    │   │   └── index.md

Have section with simple text files is common for sites. Sometimes you need to have "Contacts" or "Features" page without dynamic elements. Just simple HTML. Here are these files. By default available by `frontend.page` route, if you need to change it see inside [`frontend/views.py`](https://github.com/xen/flask-project-template/blob/master/project/frontend/views.py).

    │   ├── extensions.py

All Flask extensions registered here. You can access them by import from this file. More information is available in [configuration](#configuration) chapter.

    │   ├── frontend
    │   │   ├── __init__.py
    │   │   ├── templates
    │   │   │   └── frontend
    │   │   │       ├── index.html
    │   │   │       └── user_profile.html
    │   │   └── views.py

Front page of the site and some useful common pages combined in one blueprint. Generally each site section have its own blueprint, but if you are not sure where to put something small put it here.

    │   ├── models.py

Helper to access `SQLAlchemy` models. I found very comfortably to have all models collected together in one place. Since your models always mapped into database you never should have conflict errors using the same name because database don't allow to have several tables with the same name.

    │   ├── tasks.py

Celery tasks placed here. If you have worked with Celery you will found yourself familiar with this concept. If you need to spit tasks in different files then follow idea of `models.py`.

    │   ├── templates
    │   │   ├── base.html
    │   │   ├── counter.html
    │   │   ├── macros.html
    │   │   ├── misc
    │   │   │   ├── 403.html
    │   │   │   ├── 404.html
    │   │   │   ├── 405.html
    │   │   │   ├── 500.html
    │   │   │   └── base.html
    │   │   ├── nav.html
    │   │   └── page.html

There are basic site templates. Each blueprint have its own `template/<blueprint_name>` folder because of recommendation of Jinja documentation. If you don't want to read how Jinja environment lookup working then just follow this pattern. For your convenience `misc` folder contains templates for common error pages.   

    │   ├── translations
    │   │   ├── en
    │   │   │   └── LC_MESSAGES
    │   │   │       └── messages.po
    │   │   ├── messages.pot
    │   │   └── ru
    │   │       └── LC_MESSAGES
    │   │           ├── messages.mo
    │   │           └── messages.po

If you don't need internationalization you can ignore this folder. If you don't then your translation strings located here. `Po` files are standard for translation and internationalization of different projects. Always cover text inside `_` (underscore) function, project code contains all needed examples.

    │   └── utils.py

Trash-can for all common usefulness that can't find place in other parts of the code.

    ├── requirements.txt

All project dependencies installed by `pip`.

    ├── setup.py

This file makes your folder python project that can be wrapped into egg and distributed by DevOps. This part is not covered in documentation and usually needed on past stages of project.

    └── static
        ├── bower.json
        ├── code.js
        ├── favicon.png
        ├── libs
        ├── robots.txt
        └── style.css

All static dependencies are installed by [`bower`](http://bower.io/) packages manager. Of course you can get rid of `node.js` as dependency, but I found that full automation save vast amount of time and it is almost impossible to avoid of using popular JavaScript frameworks or compilers. Why to avoid such things as `browserify` or CoffeScript? By default site already use Bootstrap.

## Configuration

Already mention my approach: project should be able to start with minimum external dependencies. Of course if project grow up probability of using individual features increase. For example Postgres have different capabilities then SQLite, but this Flask project template trying to be as much agnostic as it can. That is why `config.py` is not empty, I attempt to make you able to start your simple Flask application after git checkout.

Of course you will make changes to your configuration, but more important how your project will work after development phase and how it flexible will be if you have team of developers. 

My recommendation store everything common and insensitive inside `config.py`. But if you need to have personal settings then store in `local.cfg` and put this file in the root folder of the project. 

But still it is not flexible enough. What if you need to connect staging or test database? Then you can use option `-c` to define different config file:

    $ python manage.py runserver -c test.cfg 
    # if you need to apply migration to test database
    $ python manage.py -c test.cfg db upgrade

This time Flask will read configuration this order:

1. `config.py` inside project folder
2. Try to find `local.cfg` in parent folder
3. Configuration file provided by command line

Notice that `cfg` files don't executed it is simple text files. In the end configuration variable will have last value it was mentioned. For example if `MAIL_SERVER` defined in `config.py` and redefined in `local.cfg` then last value will be used by Flask application.

This approach cover most cases I have in my practice. Show your DevOp how to use `cfg` and put inside variables he/she need to change. 

Also `local.cfg` is ignored in `.gitignore` so you will not accidentally put your database passwords to public repository.

## `app.py` — cornerstone part of your application


