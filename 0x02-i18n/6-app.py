#!/usr/bin/env python3
''' flask app '''

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

app = Flask(__name__)


class Config:
    ''' Babel conf '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    ''' get user based on id '''
    id = request.args.get('login_as')
    user_id = int(id)

    if user_id:
        return users.get(user_id)

    return None


@app.before_request
def before_request():
    ''' befor req '''
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' render 6-index.html page in '/' endpoint '''
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    ''' Get locale from request '''
    user_locale = request.args.get('locale', '')

    if user_locale in app.config["LANGUAGES"]:
        return user_locale

    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']

    hdr_locale = request.headers.get('locale', '')

    if hdr_locale in app.config["LANGUAGES"]:
        return hdr_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(port=5000)
