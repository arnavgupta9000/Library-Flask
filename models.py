from __init__ import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String())
    password = db.Column(db.String(100))


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
    