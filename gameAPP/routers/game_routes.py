# routers/game_routes.py
from fastapi import APIRouter, HTTPException
from models import start_new_game, get_active_game, record_guess, update_winner

router = APIRouter()

@router.post("/start-game/")
def start_game():
    game = get_active_game()
    if game:
        raise HTTPException(status_code=400, detail="A game is already active.")
    game_id = start_new_game()
    return {"message": "Game started!", "game_id": game_id}

@router.post("/guess/")
def make_guess(user_id: int, guess: int):
    if not (1 <= guess <= 10):
        raise HTTPException(status_code=400, detail="Guess must be between 1 and 10.")
    
    game = get_active_game()
    if not game:
        raise HTTPException(status_code=400, detail="No active game.")
    
    game_id = game['id']
    target_number = game['target_number']
    
    if guess == target_number:
        update_winner(game_id, user_id)
        return {"message": "Congratulations! You've won!", "winner_id": user_id}
    else:
        record_guess(game_id, user_id, guess)
        return {"message": "Wrong guess. Try again next week!"}
