from . import db #import from the init package, the db var
from flask_login import UserMixin # gives user object properties for flask Login

# creates layout for objects that will be stored in the db. saying that all notes need to look like X, all users like Y
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
