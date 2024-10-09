from flask import Blueprint, render_template, flash, request, redirect, url_for
from models import Book # sql Table
from __init__ import db
from flask_login import current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books= books) # can also pass show_nav_bar = True, as an arg and it will work

@routes.route('/books')
def books():
    return render_template('books.html')

@routes.route('/add_books', methods = ["GET", "POST"])
def add_books():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']
        description = request.form['description']
        new_book = Book(title=title, author=author, genre=genre, year=year, description = description, user_id = current_user.id)
        db.session.add(new_book)
        db.session.commit()

        flash('Book added successfully!', 'success')
        return redirect(url_for('routes.add_books'))

    return render_template('add_book.html')