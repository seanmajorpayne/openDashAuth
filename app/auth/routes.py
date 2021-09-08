from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app.auth import bp
from app.forms import LoginForm
from app.models import User
from werkzeug.urls import url_parse


def get_user():
    return current_user


@bp.route("/")
@bp.route("/index")
@login_required
def index():
    return render_template("index.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Implements the login feature for the app.
    Errors are shown if incorrect details are used. If the user tried
    to access a page requiring login without being authenticated,
    they are redirected there after sign in.
    """

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data
        ).first()  # None if invalid
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get("next")

        """To prevent malicious users from adding a malicious site into the parameters,
        this checks to see if the url is relative.
        """
        if not next_page or url_parse(next_page).netloc != "" or next_page == "/logout":
            next_page = url_for("index")
        return redirect(next_page)

    return render_template("login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
