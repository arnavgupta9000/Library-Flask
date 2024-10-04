from __init__ import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String())

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # id will autoincrement
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    avaliable = db.Column(db.Boolean, default = True)
    rating = db.Column(db.Integer, default = 5) # 5 = max score