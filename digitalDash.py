from app import app, db
from app.models import User, Data


@app.shell_context_processor
def make_shell_context():
    """ Loads database instance and models into the shell interface
    for testing. (When you run flask shell in terminal/command line)
    """
    return {'db': db, 'User': User, 'Data': Data}