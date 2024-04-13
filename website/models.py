from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import DateTime


class Errand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    faculty = db.Column(db.String(100))
    institution = db.Column(db.String(100))
    program = db.Column(db.String(100))
    term = db.Column(db.Integer)

# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#  class Reminder:
#     pass   

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    errands = db.relationship('Errand')

# class Faculty(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#
# class Institution(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#
# class Program(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)