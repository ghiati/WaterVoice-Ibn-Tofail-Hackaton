# routers/video_routes.py
from fastapi import APIRouter, UploadFile, HTTPException, Depends
from models import get_last_completed_game, save_video_path
import os
from fastapi.responses import FileResponse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()

UPLOAD_DIRECTORY = "uploads"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@router.post("/upload-video/")
async def upload_video(file: UploadFile, user_id: int):
    # Retrieve the last completed game
    game = get_last_completed_game()
    if not game:
        raise HTTPException(status_code=400, detail="No completed game found.")

    # Log the game and user details for debugging
    winner_id = game.get('winner')
    logging.info(f"Winner ID from the game: {winner_id}, User ID attempting upload: {user_id}")

    # Check if the user is the winner
    if user_id != winner_id:
        raise HTTPException(status_code=403, detail="Only the winner can upload a video.")

    # Check if a video has already been uploaded for this game
    if game.get('video_path'):
        raise HTTPException(status_code=400, detail="Video has already been uploaded for this game.")

    # Validate the file type
    file_extension = os.path.splitext(file.filename)[1]
    allowed_extensions = ['.mp4', '.mov', '.avi', '.mkv']
    if file_extension.lower() not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Unsupported file type. Allowed types: mp4, mov, avi, mkv.")

    # Save the uploaded file
    file_location = os.path.join(UPLOAD_DIRECTORY, f"{game['id']}_{file.filename}")
    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    # Update the video path in the database
    save_video_path(game['id'], file_location)
    return {"message": "Video uploaded successfully!", "file_location": file_location}

@router.get("/video/")
async def get_video():
    # Retrieve the last completed game
    game = get_last_completed_game()
    if not game or not game.get('video_path'):
        raise HTTPException(status_code=404, detail="No video uploaded.")

    video_path = game['video_path']
    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="Video file not found.")

    return FileResponse(video_path, media_type="video/mp4", filename=os.path.basename(video_path))
