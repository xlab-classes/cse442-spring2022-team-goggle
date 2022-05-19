This is the branch for the transition to Flask

# How to install the necessary packages
pip install flask
pip install flask-login
pip install beautifulsoup4
pip install pony


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


mysql -h oceanus -u ubit -p
mysql -h oceanus -u jlchugh -p

https://docs.ponyorm.org/firststeps.html
https://www.blog.pythonlibrary.org/2014/07/21/python-101-an-intro-to-pony-orm/

# How to Run the Application
0. go to www-student.cse.buffalo.edu:5009/ with the ub vpn on OR
1. install the necessary packages
2. make sure you are connected to the ubvpn and open up a terminal
3. cd into RecipeApp
4. run 'export FLASK_APP=main.py; export FLASK_DEBUG=1'
5. run 'flask run' or 'flask run --host=y.y.y.y -p xxxx' with the y's being the host and xxxx being your desired port
6. go to the address in your favorite browser
