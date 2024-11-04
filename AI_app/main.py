# main.py
from fastapi import FastAPI, HTTPException
from services.report_service import generate_report
from services.quiz_service import generate_quiz

app = FastAPI()

@app.get("/generate_report")
async def generate_report_route():
    try:
        return await generate_report()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate_quiz")
async def generate_quiz_route():
    try:
        return await generate_quiz()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
