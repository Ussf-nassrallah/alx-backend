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
def before_request() -> None:
    ''' befor req '''
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    ''' Get locale from request '''
    user_locale = request.args.get('locale', '')

    if user_locale in app.config["LANGUAGES"]:
        return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' render 5-index.html page in '/' endpoint '''
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port=5000)
