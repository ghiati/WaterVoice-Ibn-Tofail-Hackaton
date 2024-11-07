from flask import Blueprint, request, jsonify,render_template,session,redirect,url_for,current_app,flash
from .model import User,Rapport, GameResult,VideoG
from .form import VideoUploadForm
from flask_login import current_user, login_user,login_required
from . import db
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime,timedelta

import os
from werkzeug.utils import secure_filename



route = Blueprint('route', __name__)


WINNING_NUMBER =9



@route.route("/home")
@login_required
def home():
    return render_template('index1.html', title="Home")

@route.route("/ report", methods=["GET", "POST"])
@login_required
def rappore():
    report_data = {}
    
    
    try:
        # Envoyer une requête au route /generate_report dans ai_app
        response = requests.get("http://127.0.0.1:5000/generate_report")
        
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            report_data = response.json()  # Extraire les données du rapport depuis la réponse JSON
            report_text = report_data.get('report', '')  # Obtenir le texte du rapport
            
            # Nettoyer le texte
            clean_report = clean_text(report_text)
        else:
            clean_report = "Échec de la récupération des données du rapport"
    except requests.exceptions.RequestException as e:
        clean_report = f"Erreur: {str(e)}"

    # Passer le texte nettoyé au template
    return render_template('rapore.html', title="Rappore", x=clean_report)

def clean_text(text):
    # Remplacer les balises ** par des sauts de ligne et nettoyer le texte
    text = text.replace('**', '').replace('\n', '<br>')  # Enlever les ** et ajouter des <br> pour les sauts de ligne dans HTML
    return text.strip()  # Nettoyage final


# @route.route("/create_post")
# @login_required
# def create():
    
#     return render_template('create.html', title="create ")
# -----------------------------------------------------

@route.route('/create_post')
def index():
    # Compte à rebours pour la fin de la seroutee
    next_reset = session.get('next_reset', datetime.now() + timedelta(days=7))
    return render_template('index.html', next_reset=next_reset)

@route.route('/jeu')
@login_required
def jeu():
    # Get the start and end of the current week
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())  # Start of the week (Monday)
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)  # End of the week (Sunday midnight)
    
    # Check if the player has already played this week
    # if current_user.last_game_attempt and start_of_week < current_user.last_game_attempt < end_of_week and is_sunday_night():
        # return redirect(url_for('route.index'))  # The player cannot play more than once a week
    
    # Check if there is a winner this week
    # if reset_jeu_winner():
        # return redirect(url_for('route.index'))  # The player has already won and cannot play again
    
    # If none of the above conditions are met, the player can play
    return render_template('jeu.html')





def is_sunday_night():
    today = datetime.now()
    
    # Check if today is Sunday
    if today.weekday() == 6:  # Sunday is 6 in Python's weekday() (Monday=0, Sunday=6)
        # Check if the time is 23:59:59
        if today.hour == 23 and today.minute == 59 and today.second == 59:
            return True
    return False

# Test the function
if is_sunday_night():
    print("Today is Sunday at 23:59:59")
else:
    print("Today is not Sunday at 23:59:59")


def reset_jeu_winner():
    cont = False
    for user in User.query.all():
       if user.is_winner == True:
            cont = True
    return  cont   
            
    


@route.route('/soumettre_resultat', methods=['POST'])
@login_required
def soumettre_resultat():
    score = int(request.form['score'])
    print(score)
    # Vérifie si le joueur a gagné
    if score == WINNING_NUMBER:
        current_user.is_winner = True
        db.session.commit()
        # Si l'utilisateur n'a pas gagné, il est marqué comme ayant joué
        current_user.last_game_attempt = datetime.now()
        db.session.commit()
        return redirect(url_for('route.create_video')) 
    else:
        flash("An error occurred while saving the video: ", "danger")
           
        return redirect (url_for('route.jeu')) 
      
        # Dirige l'utilisateur vers la page de création de vidéo
 

    # Si l'utilisateur n'a pas gagné, il est marqué comme ayant joué






def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
@route.route('/create_video', methods=['GET', 'POST'])
@login_required
def create_video():
    if has_user_uploaded_video(current_user.id):
        flash("لقد قمت برفع فيديو من قبل!", "info")
        return redirect(url_for('route.index'))
    # Redirect if the user is not a winner
    if not current_user.is_winner:
        return redirect(url_for('route.index'))
    
    form = VideoUploadForm()
    
    if form.validate_on_submit():
        title = form.title.data
        video = form.video.data

        # Check if video file type is allowed
        if video and allowed_file(video.filename):
            # Secure the filename to avoid directory traversal attacks
            filename = secure_filename(video.filename)

            # Ensure the upload folder exists
            upload_folder = current_app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)  # Create the folder if it doesn't exist

            # Save the video file to the upload folder
            try:
                video_path = os.path.join(upload_folder, filename)
                video.save(video_path)
                
                # Create a new VideoG record in the database
                new_video = VideoG(user_id=current_user.id, title=title, video_filename=filename)
                db.session.add(new_video)
                db.session.commit()

                flash("Video uploaded successfully!", "success")
                return redirect(url_for('route.index'))
            except Exception as e:
                flash(f"An error occurred while saving the video: {e}", "danger")
                print(f"Error saving file: {e}")
        else:
            flash("Invalid file type. Please upload a valid video file.", "danger")

    return render_template('creer_video.html', form=form)
    
def has_user_uploaded_video(user_id):
    # تحقق إذا كان هناك أي فيديو مرتبط بهذا المستخدم في قاعدة البيانات
    return db.session.query(VideoG.id).filter_by(user_id=user_id).first() is not None

# =======================================================
def reset_jeu():
    db.session.query(GameResult).delete()
    db.session.commit()
    for user in User.query.all():
        user.is_winner = False
    db.session.commit()

def verifier_gagnant():
    top_result = GameResult.query.order_by(GameResult.score.desc()).first()
    
    if top_result and top_result.user_id == current_user.id:
        current_user.is_winner = True
        db.session.commit()
#============================== 

@route.route("/about")
def about():
    return render_template('about.html', title="about ")
@route.route("/home_post", methods=['POST'])
def home_post():

    
    return render_template('route.index', title="home post ")
