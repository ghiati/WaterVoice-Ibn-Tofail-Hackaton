from . import db
from flask_login import UserMixin
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm

class User(db.Model, UserMixin):  # Ensure UserMixin is inherited
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.numero}>'
    

