# Dash Multi-User Authentication

Dash does not natively support multi-user authentication (at least not for free). While
looking for a solution to support my own app, I noticed many developers online needed
the ability to support dedicated viewpoints for individual users, but the official forums
provided little to no help.

As far as I'm aware, this is the only free and publicly available solution to support
multiple users within Dash (at least that is useful in a real-world application).

## How it Works

Since Dash is built on top of Flask, this application uses Flask as the primary server
and serves Dash as an embedded app.

This adds more benefits on top of login functionality, as this allows for the construction
of a full-fledged application in addition to the dashboard view.

Flask's login-manager is used to manage the user's session. Normally, in a Flask app,
routes.py defines all of the URL-page mappings. This is also where the current-user is
identified to securely serve content based on whether or not the user is logged in. 

By creating a method within routes that returns the current-user, one can import and 
reference this user in Dash, allowing for database queries based on the individual user 
(while simultaneously preventing the user from getting access to other user's data).

![demo gif](https://github.com/seanmajorpayne/dash_multi_user_authentication/blob/master/auth_demo.gif)

## Getting Started

Simply perform a git pull to grab the files from this repo.

```
git clone https://github.com/seanmajorpayne/dash_multi_user_authentication
```

Open your terminal and navigate to the main application folder

```
$ cd /path/to/dash_multi_user_authentication
# The command on windows is 'dir' not 'cd'
```

You will probably want to run this application in a virtual environment. Create one with
the following command:

```
python3 -m venv venv
```

Then run it with:

```
source venv/bin/activate
```

Next, install the dependencies.

```
pip install -r requirements.txt
```

Note that some dependencies will only install with an older version of pip. If you are
getting an error about 'PEP 517', run the following command:

```
pip install pip==18.1 && pip install -r requirements.txt && pip install pip --upgrade
```

This will downgrade your current pip version and upgrade it back once the dependencies
are installed.

Once all of this is done, you can run the application locally using 

```
MAIL_SERVER=example.com FLASK_APP=$PWD/digitalDash.py flask run
```

or modify it and deploy it on a public facing server.

The app is configured with a single user 'john' and password 'pw' which you
can use to see the functionality provided by the app. You can add more users easily
through the database. Note that the config file currently has a secret key that
always amounts to true. This needs to be changed for a production application.

## Security

While this template is offered 'as is' and I don't make any guarantees about security,
there are a few helpful security features included. Flask-WTF forms have CSRF protection
by default. Flask configures Jinja2 to automatically escape values unless explicitly told
not to, which helps with cross site scripting issues.

For a full overview of Flask Security, check [here](https://flask.palletsprojects.com/en/1.1.x/security/)

## Contributions

Pull requests are welcome.

## License
See the license details [here](https://github.com/seanmajorpayne/dash_multi_user_authentication/blob/master/LICENSE.md)

## Acknowledgements

Thank you to Miguel Ginsberg for the [Flask Mega Tutorial.](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## To Do
- [x] Add requirements.txt
- [x] Add License
- [ ] Clean up Bootstrap Styling
