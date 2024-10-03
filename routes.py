from flask import Blueprint, render_template
from models import Book # sql Table

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('base.html')

@routes.route('/books')
def books():
    return render_template('books.html')

