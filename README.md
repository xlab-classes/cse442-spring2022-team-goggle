This is the branch for the transition to Flask

# How to install the necessary packages
pip install flask
pip install flask-login
pip install flask-sqlalchemy
pip install beautifulsoup4

Versions:
Python                 3.8.10
Flask                  2.1.1
Flask-Login            0.6.0
Flask-SQLAlchemy       2.5.1
beautifulsoup4         4.10.0

# accessing on the department server https://wiki.cse.buffalo.edu/services/content/flask
1. set up ubvpn and connect
2. ssh ubit@cheshire.cse.buffalo.edu
3. cd /web/...../cse442e
4. (set up virtual environment if its not already there)  python3.8 -m venv venv
5. bash
6. . venv/bin/activate
7. cd in to cse442_goggle_whatever/ recipeapp
8. export FLASK_APP=main.py
   export FLASK_DEBUG=1
9. flask run --host=0.0.0.0 -p 5009 or whatever port you want
10. visit http://www-student.cse.buffalo.edu:5009/ or whatever port


todo:
https://hackersandslackers.com/flask-sqlalchemy-database-models/

create models for: users, ingredients, recipes
each recipe gets a list of ingredients
connect the flask application to the oceanus mysql 
