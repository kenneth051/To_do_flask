"""Module for application factory."""
# System libraries
from os import getenv

# Third-party libraries
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restplus import Api


from config import config, Config

config_name = getenv('FLASK_ENV', default='production')


def create_app(config=config[config_name]):
    """Return app object given config object."""
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False



    return app
