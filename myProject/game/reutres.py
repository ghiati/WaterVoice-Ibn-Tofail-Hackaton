from flask import Blueprint, render_template, url_for, flash, redirect,request
from werkzeug.security import generate_password_hash
from myProject import db,bcrypt
from myProject.model import User
from myProject.form import RegistrationForm,LoginForm
from flask_login import current_user, login_user,login_required
from email_validator import validate_email, EmailNotValidError





game = Blueprint('game', __name__)

