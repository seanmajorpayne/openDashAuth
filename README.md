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

For now, you will need to install the dependencies manually. I will add a requirements
file soon for easy install.

Note that some dependencies will only install with an older version of pip. If you are
getting an error about 'PEP 517', run the following command:

```
pip install pip==18.1
```

Then install the dependencies and when you are done, re-upgrade pip using:

```
pip install pip --upgrade
```

Once all of this is done, you can run the application locally using 'flask run' or
modify it and deploy it on a public facing server.

The app is configured with a single user 'john' and password 'pw' which you
can use to see the functionality provided by the app. You can add more users easily
through the database.

## License
To be added

## To Do
[ ] Add requirements.txt
[ ] Add License
[ ] Clean up Bootstrap Styling