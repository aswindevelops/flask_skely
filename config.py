import urllib
import os


class Config(object):
    SECRET_KEY = 'huoumTvxhOUGOUgr387r06)*^*^&E$gdqhd'
    DEBUG = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ""


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    pass

