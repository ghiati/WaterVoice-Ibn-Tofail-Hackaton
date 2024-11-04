# main.py
from fastapi import FastAPI
from routers import game_routes, video_routes
from database import init_db

app = FastAPI()

# Initialize the database when the application starts
init_db()

# Include routers for different functionalities
app.include_router(game_routes.router)
app.include_router(video_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Weekly Guessing Game!"}
