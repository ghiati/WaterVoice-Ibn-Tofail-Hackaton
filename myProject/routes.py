from flask import Blueprint, request, jsonify,render_template
from .model import User
from flask_login import current_user, login_user,login_required
from . import db

route = Blueprint('route', __name__)


@route.route("/home")
@login_required
def home():
    return render_template('index1.html', title="Home")
@route.route("/rappore",methods=["GET", "POST"])
@login_required
def rappore():
    x = "Contenu de votre rapport"  # Remplacez ceci par le contenu réel de votre rapport
    return render_template('rapore.html', title="rappore", x=x)

@route.route("/create_poste")
@login_required
def create():
    
    return render_template('create.html', title="create ")

@route.route("/about")
def about():
    return render_template('about.html', title="about ")
