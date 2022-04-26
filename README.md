This is the branch for the transition to Flask

# How to install the necessary packages
pip install flask
pip install flask-login
pip install beautifulsoup4
pip install lxml
pip install pony
pip install flashtext (for populate_oceanus)

Versions:
Python                 3.8.10
Flask                  2.1.1
Flask-Login            0.6.0
Flask-SQLAlchemy       2.5.1
beautifulsoup4         4.10.0
Flask-MySQL            1.5.2

# accessing on the department server https://wiki.cse.buffalo.edu/services/content/flask
1. set up ubvpn and connect
2. ssh ubit@cheshire.cse.buffalo.edu
3. cd /web/...../cse442e
4. (set up virtual environment if its not already there)  python3.8 -m venv venv
5. bash
6. . venv/bin/activate
7. cd in to cse442_goggle_whatever/ recipeapp
8. export FLASK_APP=main.py
   export FLASK_DEBUG=1                                         export FLASK_APP=main.py; export FLASK_DEBUG=1
9. flask run --host=0.0.0.0 -p 5009 or whatever port you want
10. visit http://www-student.cse.buffalo.edu:5009/ or whatever port

# some random sql stuff
mysql -h oceanus -u jlchugh -p

SHOW DATABASES;
USE cse442_2022_spring_team_e_db;
SHOW TABLES;
drop table table name;
SELECT * FROM user
SET FOREIGN_KEY_CHECKS = 0
drop table ingredient; drop table ingredient_recipe; drop table recipe; drop table recipe_user; drop table user; 


# pony resources
https://docs.ponyorm.org/firststeps.html
https://www.blog.pythonlibrary.org/2014/07/21/python-101-an-intro-to-pony-orm/
