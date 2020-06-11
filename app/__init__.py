from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask_bootstrap import Bootstrap


"""Create Flask Application"""
app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

""" Dash must be initialized within a method. The flask app is passed in as
Dash's server, allowing Dash to run within Flask, rather than as a standalone app.
This is essential for having multi-user authentication.
"""
with app.app_context():
	from app.plotlydash.dashboard import create_dashboard
	app = create_dashboard(app)

"""Errors for the production application are handled via email"""
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
	
""" Must remain at bottom of file
Routes defines URL paths
Models defines structure of database
Errors handles 404, 500 issues"""
from app import routes, models, errors