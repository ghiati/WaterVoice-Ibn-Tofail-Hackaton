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
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
#     return app
# myProject/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "main.login"  # Adjust to your login route
login_manager.login_message_category = "info"

def create_app():
    app = Flask(__name__)
    from myProject.config import Config
    # app.config.from_object('config.Config') 
    # app.config.from_object('myProject.config.Config')
    app.config.from_object(Config)
 
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

    from myProject.routes import  reset_jeu


    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_jeu, 'interval', weeks=1)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))

    return app

