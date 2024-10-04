from flask import Blueprint, render_template, redirect, url_for, flash, request
from __init__ import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

from flask_login import login_user, login_required, logout_user, current_user # for user interactions ; why we needed usermixing in models file -> for current_user;


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == "POST":
        print(f"SECRET_KEY: {current_app.config['SECRET_KEY']}")  # For debugging

        email = request.form["email"]
        name = request.form["name"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        print(f"Email to check: {email}")  # This will print the email to the terminal/console
        user= User.query.filter_by(email=email).first() # email already exists in database so they must sign in!
        if user:
            flash("Email already exists. Please sign in!" )
            return redirect(url_for('auth.register')) # redirect(url_for) just makes the webpage reload

        # add other checks

        # generate the new user
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
        
        #commit to db
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user, remember= True)
        flash("Account created" )
        return redirect(url_for('routes.home'))




    return render_template('register.html',user=current_user)