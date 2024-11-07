from . import db
from flask_login import UserMixin
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_wtf import FlaskForm

class User(db.Model, UserMixin):  # Ensure UserMixin is inherited
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # ---------------
    is_winner = db.Column(db.Boolean, default=False)
    last_game_attempt = db.Column(db.DateTime, nullable=True)
   


    def __repr__(self):
        return f'<User {self.numero}>'
    

class Rapport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(10000), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) 

# ------------
class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)    


class VideoG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=True)
    video_filename = db.Column(db.String(200), nullable=True)  # To store the filename of the uploaded video
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('videos', lazy=True))

    def __repr__(self):
        return f"<VideoG {self.title} by User {self.user_id}>"