import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "a_secure_secret_key")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload configurations
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'mkv'}  # Allowed video file types
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # Limit to 100MB file size
