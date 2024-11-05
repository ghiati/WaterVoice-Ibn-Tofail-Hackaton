# # __init__.py
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from .config import Config

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)  # Initialize the database with the app

#     # Import and create tables for models
#     from .model import User
#     with app.app_context():
#         db.create_all()  # Create tables
       

#     # Register blueprints
#     from myProject.main.route import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app
# myProject/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "main.login"  # Adjust to your login route
login_manager.login_message_category = "info"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'a_secure_random_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info' 
    from .model import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    from myProject.main.route import main as main_blueprint
    from myProject.routes import route
    # from game.routes import game
    app.register_blueprint(main_blueprint)
    app.register_blueprint(route)
    # app.register_blueprint(game)

    return app

