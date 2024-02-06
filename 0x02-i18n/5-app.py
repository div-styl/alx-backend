#!/usr/bin/env python3
"""Basic route in flask app"""
from typing import (
    Dict,
    Union
)
from flask import Flask
from flask import render_template
from flask import request, g
from flask_babel import Babel


class Config(object):
    """class for babel config for languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """return the local request object"""
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """eturns a user dictionary or None if the
    ID cannot be found or if login_as was not passed.
    """
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """
    decorator to make it be executed before all other functions.
    before_request should use get_user to find a user if any,
    and set it as a global on flask.g.user.
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route("/", strict_slashes=False)
def index() -> str:
    """render the 0-index.html template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
