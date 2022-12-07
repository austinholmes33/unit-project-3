from flask import Flask, render_template, redirect, flash, request
from flask import FlaskForm
from wtforms import PasswordField, StringField, validators
from forms import LoginForm

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login ():
    form = LoginForm(request.form)
    return render_template("login.html", form=form)