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
        flash("logged in", category='success')
        return redirect(url_for('views.home'))

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash("registered", category='success')
        return redirect(url_for('views.home'))
    return render_template("register.html")
