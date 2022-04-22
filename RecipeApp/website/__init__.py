from flask import Flask

def create_app():
    app = Flask(__name__)
    # MAKE SURE TO CHANGE THIS WHEN IT RUNS ON THE DEPARTMENT SERVER
    app.config['SECRET_KEY'] = 'jflsiejwlkjsdf'

    # import the views
    from .views import views
    from .auth import auth

    #register the views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')



    return app
