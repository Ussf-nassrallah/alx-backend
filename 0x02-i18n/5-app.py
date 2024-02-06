#!/usr/bin/env python3
''' flask app '''

from flask import Flask, render_template, request
from flask_babel import Babel

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


def get_user():
    ''' get user based on id '''
    id = request.args.get('login_as')
    user_id = int(id)

    if user_id:
        return users.get(user_id)

    return None


def before_request() -> None:
    ''' befor req '''
    current_user = get_user()
    g.current_user = current_user


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' render 4-index.html page in '/' endpoint '''
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    ''' Get locale from request '''
    user_locale = request.args.get('locale', '')

    if user_locale in app.config["LANGUAGES"]:
        return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(port=5000)
