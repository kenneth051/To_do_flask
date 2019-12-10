"""Module with application entry point."""

# System imports
from os import getenv

from flask import jsonify

# Local Imports
from main import create_app
from config import config


# get flask config name from env or default to production config
config_name = getenv('FLASK_ENV', default='production')

# create application object
app = create_app(config[config_name])


@app.route('/')
def index():
    """Process / routes and returns 'Welcome to flask boiler plate' as json."""
    return jsonify(dict(message='Welcome to flask boiler plate'))


if __name__ == '__main__':
    app.run()
