from flask import Blueprint, render_template, url_for, flash, redirect,request
from werkzeug.security import generate_password_hash
from myProject import db,bcrypt
from myProject.model import User
from myProject.form import RegistrationForm,LoginForm
from flask_login import current_user, login_user,login_required
from email_validator import validate_email, EmailNotValidError

main = Blueprint('main', __name__)

@main.route('/',methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("You have been logged in!", "success")
            return  redirect(url_for('main.home'))
        else:
            flash("Login Unsuccessful. Please check your email and password.", "danger")
    return render_template("login.html", title="Login", form=form)






@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            # Validate the email format
            valid_email = validate_email(form.email.data)
            email = valid_email.email  # This will give you the normalized email
        except EmailNotValidError as e:
            # If the email is not valid, flash an error and return to the form
            flash(str(e), 'danger')
            return render_template('registre.html', form=form)

        # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
              # Add this line before rendering the template

            flash('Email already exists! Please choose a different one.', 'danger')
            return render_template('registre.html', form=form)

        # Check if the phone number already exists
        existing_user_num = User.query.filter_by(numero=form.numero.data).first()
        if existing_user_num:
            flash('Phone number already exists! Please choose a different one.', 'danger')
            return render_template('registre.html', form=form)

        # If all checks pass, create the user
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            numero=form.numero.data,
            address=form.address.data,
            email=form.email.data,  # Use the validated and normalized email
            password=hashed_password  # Hashing the password
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('main.login'))

    return render_template('registre.html', form=form)
@main.route("/home")
@login_required
def home():
    return render_template('index.html', title="Home")
