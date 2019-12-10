"""Application configuration module."""
from os import getenv


class Config(object):
    """App base configuration."""

    SQLALCHEMY_DATABASE_URI = getenv(
        "DATABASE_URI", default="postgresql://localhost/boilerplate"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    """App production configuration."""

    pass


class DevelopmentConfig(Config):
    """App development configuration."""

    DEBUG = True


class TestingConfig(Config):
    """App testing configuration."""

    TESTING = True


config = {
    "development": DevelopmentConfig,
    "staging": ProductionConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
