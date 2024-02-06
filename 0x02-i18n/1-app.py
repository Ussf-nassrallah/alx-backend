#!/usr/bin/env python3
''' flask app / Basic Babel setup '''

from flask import Flask, render_template
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
def index():
    ''' render 1-index.html page in '/' endpoint '''
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000)
