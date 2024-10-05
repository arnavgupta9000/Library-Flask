'''
difference between 

return redirect(url_for('routes.home'))

return render_template('home.html')

return url_for('routes.home')

the first one is used when making post requests, it reloads the page thus allowing things like usermixin to work properly (client-side action)
when to use? after form submission, after a specific action(like logging out, deleting, signing in), to change url path

the second one is used when making get requests, cause the page does not need to be reloaded and we can just go the we page (server-side action, no URL change keeps the html)
When a user visits a page (like /home or /profile) and you want to show the content without triggering a new HTTP request, for static pages, If there's an error in a form submission (like a missing field) you can stay on the same page and show the error message without redirecting.


the third one is used when u just want to just want to generate a URL and possibly pass it into a function, log it, or use it in a template, but notice no rendering or redirecting is happening (Generates and returns a URL string without doing anything else)
It's typically used internally to generate URLs dynamically (so only used when specifying paths basically)
'''


from flask import Blueprint, render_template, redirect, url_for, flash, request
from __init__ import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

from flask_login import login_user, login_required, logout_user, current_user # for user interactions ; why we needed usermixing in models file -> for current_user;


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user: # email exists just check to make sure the password matches
            if check_password_hash(user.password, password):
                login_user(user)
                flash("Log in successful")
                return redirect(url_for("routes.home"))
            else:
                flash("Incorrect password")
        else:
            flash("No account found with that email")
            

    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('routes.home'))

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