from flask import Flask, render_template, redirect, flash, request
from flask import FlaskForm
from wtforms import PasswordField, StringField, validators
from forms import LoginForm
from flask import session
import customers

app = Flask(__name__)

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])


@app.route("/login", methods=["GET", "POST"])
def login ():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = customers.get_by_username(username)

        if not user or user['password'] != password:
            flash("Invalid username or password")
            return redirect("/login")

        session["username"] = user["username"]
        flash("Logged in")
        return redirect("/melons")

    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    del session["username"]
    flash("Logged out.")
    return redirect("/login")