from flask import Flask
from flask_sqlalchemy import SQLAlchemy # for the sql
from flask_login import LoginManager # for handling the logging in 
from os import path
import os



db = SQLAlchemy()
db_name = "database.db"


login_manager = LoginManager()  # login handler that manages users (like logout and managing user sessions)
login_manager.login_view = 'auth.login' # this tells us where to redirect to (like if a page is required for a user to be logged in and their not it send u to this page)

# User loader function
@login_manager.user_loader # basically when a user is in a session, evertime they make a request they need an id, this gives us that 
def load_user(user_id): # this allows the "current_user" to work properly
    from models import User, Book  
    return User.query.get(int(user_id)) # takes id and then returns the corresponding user


def create_app():
    app = Flask(__name__)
    print("Flask app is being initialized")  # Debugging line
    app.config['SECRET_KEY'] = 'this secret key will be longer then most to differentiate'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}' # init the db as "databse.db"

    print(f"SECRET_KEY in create_app: {app.config['SECRET_KEY']}")


    db.init_app(app) # make the database
    login_manager.init_app(app)  # attach the login manager to the app
    from models import User, Book
    create_database(app)


    # register the blueprints (that are made from other files) allows us to be able to use these routes.
    from auth import auth as auth_blueprint
    from routes import routes as routes_blueprint 
    app.register_blueprint(auth_blueprint, url_prefix = '/')
    app.register_blueprint(routes_blueprint, url_prefix = '/')

    return app

def create_database(app):
    # if os.path.exists(db_name):
    #     os.remove(db_name)  # Deletes the existing database file
    if not path.exists('database.db'):

        with app.app_context(): # makes the application context -> flask doesnt doesn't automatically know which application is "active" unless you explicitly push the application context 
            db.create_all() 
            
    print('Created databse')

