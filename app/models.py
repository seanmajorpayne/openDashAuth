from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

"""
Defines all of the database models used.
"""

class User(UserMixin, db.Model):
	
    """ Defines the models for a user. Passwords are hashed for security and
    not stored directly. This inherits from db.Model (base class from SQLAlchemy)
	
    UserMixin adds four generic implementations from FlaskLogin
    is_authenticated - True if user's credentials are valid
    is_active - True if user's account is active
    is_anonymous - False for regular users, True for special anon users
    get_id() - returns unique id for the user
    """
	
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    data_for_user = db.relationship('Data', backref='user_data', lazy='dynamic')
	
    def set_password(self, password):
        """ Allows a user to create a password, creates a hash for the password
        and stores it in the database.
        """
        self.password_hash = generate_password_hash(password)
	
    def check_password(self, password):
        """ Allows the application to check a supplied password against the hash
        stored in the database. Returns true if they are the same.
        """
        return check_password_hash(self.password_hash, password)
	
    def __repr__(self):
        """ Tells Python how to print the model (for debugging purposes) """
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    """ FlaskLogin is unaware of databases, so this function
    helps load the user given an id.
    """
    return User.query.get(int(id))


class Data(db.Model):
    """
    This is a sample data class. Replace this with whatever database structure
    you prefer to use for the application.
    """
    x1 = db.Column(db.Integer, primary_key=True)
    x2 = db.Column(db.Integer, primary_key=True)
    x3 = db.Column(db.Integer, primary_key=True)
    y1 = db.Column(db.Integer, primary_key=True)
    y2 = db.Column(db.Integer, primary_key=True)
    y3 = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
    def __repr__(self):
        return '<Data {}>'.format(self.x1)