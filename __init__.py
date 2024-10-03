from flask import Flask
from flask_sqlalchemy import SQLAlchemy # for the sql
from flask_login import LoginManager # for handling the logging in 
from os import path

db = SQLAlchemy()

login_manager = LoginManager()  # login handler, and
login_manager.login_view = 'auth.login' # this tells us where to redirect to

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'this secret key will be longer then most to differentiate' 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # init the db as "databse.db"

    db.init_app(app) # make the database

    create_database(app)

    # register the blueprints (that are made from other files) allows us to be able to use these routes.
    from auth import auth as auth_blueprint
    from routes import routes as routes_blueprint 
    app.register_blueprint(auth_blueprint, url_prefix = '/')
    app.register_blueprint(routes_blueprint, url_prefix = '/')

    return app

def create_database(app):
    if not path.exists('database.db'):
        with app.app_context(): # makes the application context -> flask doesnt doesn't automatically know which application is "active" unless you explicitly push the application context 
            db.create_all() 
        print('Created databse')

