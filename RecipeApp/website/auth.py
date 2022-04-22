from flask import Blueprint, render_template, request, flash

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
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')

    return render_template("register.html")
