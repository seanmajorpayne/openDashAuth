from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
migrate = Migrate()
bootstrap = Bootstrap()


def create_app():
    # Create Flask Application
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    # Initialize Blueprints
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # Errors for the production application are handled via email
    if not app.debug:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Dash App Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/digitaldash.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Dash App Startup')

    # app will be used as the server for Dash
    return app
