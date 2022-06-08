import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

CURRENT_ENV = os.getenv("FLASK_ENV")


db = SQLAlchemy()

login_manager = LoginManager()


def create_app():
    """
    Function to create a Flask application object.
    @return:
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if CURRENT_ENV == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif CURRENT_ENV == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        # default is development
        app.config.from_object('config.DevelopmentConfig')

    register_extensions(app)

    register_blueprints(app)

    register_error_handlers(app)

    return app


def register_extensions(app):
    """
    Function to register the Flask extensions
    @param app: Flask application object
    """

    db.init_app(app)

    login_manager.init_app(app)


def register_blueprints(app):
    """
    Function to register Flask blueprints
    @param app: Flask application object
    """
    from averich.blueprints.user.controller import user_blueprint

    app.register_blueprint(user_blueprint)


def register_error_handlers(app):
    """
    Function to register Flask error handlers.
    @param app: Flask application object
    """
    from averich.generic.error_handlers import handle_401, handle_404, handle_405, handle_500

    app.register_error_handler(401, handle_401)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(405, handle_405)
    # If the PROPAGATE_EXCEPTION is False, Flask will treat it as internal server error including exceptions.
    # The following method will only be called when PROPAGATE_EXCEPTION is False.
    # app.register_error_handler(500, handle_500)
    # If PROPAGATE_EXCEPTION is True, Flask will treat it as exception and call the following method
    # The following method will be called when PROPAGATE_EXCEPTION is True or False
    app.register_error_handler(Exception, handle_500)
