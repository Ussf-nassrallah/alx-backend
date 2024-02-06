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


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' render 4-index.html page in '/' endpoint '''
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    ''' Get locale from request '''
    query_params = request.query_string.decode('utf-8').split('&')

    query_params_dict = dict(map(
        lambda param: (
            param if '=' in param else '{}='.format(param)
        ).split('='),
        query_params,
    ))

    if 'locale' in query_params_dict:
        if query_params_dict['locale'] in app.config["LANGUAGES"]:
            return query_params_dict['locale']

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(port=5000)
