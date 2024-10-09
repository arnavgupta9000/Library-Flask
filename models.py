from __init__ import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String())
    password = db.Column(db.String(100))
    books = db.relationship('Book', backref='user', lazy=True)
    # books = db.relationship('Book') => one to many relationship, ie 1 user many books,
    #This creates a bidirectional relationship.
    # From the User side: Each user can access all the books they've added by doing something like user.books.
    # From the Book side: Each book can access the user who added it via the user attribute, like book.user.
    # Essentially, backref='user' automatically adds a user property to the Book model, allowing you to access the related user from any book record.




class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # id will autoincrement
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(1000), default = None)
    content = db.Column(db.String(150000), default = None)
    avaliable = db.Column(db.Boolean, default = True)
    rating = db.Column(db.Integer, default = 5) # 5 = max score
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Assuming your User model has an 'id'

    