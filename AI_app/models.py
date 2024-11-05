# models.py
from typing import List

class Choice:
    def __init__(self, option: str, text: str):
        self.option = option  # e.g., "A", "B", "C", "D"
        self.text = text      # The actual choice text

class Question:
    def __init__(self, question_text: str, choices: List[Choice], correct_answer: str):
        self.question_text = question_text  # The text of the question
        self.choices = choices                # List of Choice objects
        self.correct_answer = correct_answer  # The correct answer option

