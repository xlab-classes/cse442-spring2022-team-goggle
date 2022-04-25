from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from pony.orm import *
import pony.orm as pny
import pdb


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html", name="example name")


@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        pdb.set_trace()
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        with pny.db_session:
            new_user = User(email=email, first_name=firstName, last_name=lastName, password=generate_password_hash(password, method='sha256'), )
    return render_template("register.html")
