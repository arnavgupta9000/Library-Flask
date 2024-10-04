from flask import Blueprint, render_template
from models import Book # sql Table

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html') # can also pass show_nav_bar = True, as an arg and it will work

@routes.route('/books')
def books():
    return render_template('books.html')

