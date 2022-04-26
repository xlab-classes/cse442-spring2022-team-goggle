from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from pony.orm import *
import pony.orm as pny
import pdb


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        with pny.db_session:
            user = User.get(email=email)
        if user:
            if check_password_hash(user.password, password):
                flash("logged in", category='success')
                return redirect(url_for('views.home'))
            else: flash("Incorrect email or password.", category='error')
        else:
            flash("incorrect password", category='error')
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html", name="example name")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')

        with pny.db_session:
            user = User.get(email=email)
        if user:
            flash('Email already in use', category='error')
        else:
            with pny.db_session:
                new_user = User(email=email, first_name=firstName, last_name=lastName,
                                password=generate_password_hash(password, method='sha256'),)
            flash("registered", category='success')
            return redirect(url_for('views.home'))
    return render_template("register.html")
