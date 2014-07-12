# Flask project template

`Flask project template` contains working example of Flask project with features:

- Easy to fork/setup Flask project template
- SQLAlchemy with out-of-the-box migrations (uses Alembic)
- Simple setup `make setup & make run` which make local virtualenv isolated environment and doesn't trash your system python.
- Contains `Dockerfile` that allow to setup full linux environment on any host OS supported by Docker
- Static managed by `bower`. By default templates uses `Bootstrap` but doesn't force you to use this UI framework.
- Have working example of GitHub OAuth authorization, you only need to provide your own security and secret key (will work with example keys only on `localhost:5000`). Allow user login/logout 
- Integrated Babel support and special support targets for `make`
- User settings page with ability to switch site language
- `Flask-FlatPages` support to simplify static pages management
- Builtin `Flask-Script` support with shell

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
