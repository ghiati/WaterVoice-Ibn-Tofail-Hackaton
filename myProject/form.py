from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from flask_login import current_user
from .model import User

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', 
                             validators=[DataRequired(), Length(min=2, max=50)],
                             render_kw={"placeholder": "First Name", "class": "input-box"})
    
    last_name = StringField('Last Name', 
                            validators=[DataRequired(), Length(min=2, max=50)],
                            render_kw={"placeholder": "Last Name", "class": "input-box"})
    
    address = StringField('Address', 
                            validators=[DataRequired(), Length(min=5, max=100)],
                            render_kw={"placeholder": "Address", "class": "input-box"})
    
    numero = StringField('Number', 
                         validators=[DataRequired(), Length(min=10, max=15),
                                     Regexp(r'^\+?[0-9]*$', message="Invalid phone number. Only digits and optional '+' allowed.")],
                         render_kw={"placeholder": "Phone Number", "class": "input-box"})
    
    email = StringField('Email', 
                        validators=[DataRequired(), Email(), Length(max=120)],
                        render_kw={"placeholder": "Email", "class": "input-box"})
    
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=6, max=200)],
                             render_kw={"placeholder": "Password", "class": "input-box"})
    
    submit = SubmitField('Sign Up', render_kw={"class": "btn"})

    def validate_email(self, email):
        # Only check for email existence if the user is authenticated
        if current_user.is_authenticated:
            if email.data != current_user.email:
                user = User.query.filter_by(email=email.data).first()
                if user:
                    raise ValidationError("Email already exists! Please choose a different one.")
        else:
            # If the user is not authenticated, just check for email existence
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email already exists! Please choose a different one.")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
