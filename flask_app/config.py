import os
from pathlib import Path


class Config(object):
    DEBUG = False
    SECRET_KEY = 'NyLa8GgOgNsgLanRvKcGCw'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_PATH = Path(__file__).parent.parent.joinpath("data")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(DATA_PATH.joinpath('data.sqlite'))
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True