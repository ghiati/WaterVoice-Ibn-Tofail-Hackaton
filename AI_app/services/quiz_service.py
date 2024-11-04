from typing import List, Dict
from services.report_service import generate_report
from config import model

# Step 1: Generate questions with correct answers only
async def generate_questions_with_correct_answers() -> List[Dict[str, str]]:
    report = await generate_report()
    report_content = report.get("report", "")
    
    # Prompt to generate questions with only correct answers
    quiz_prompt = f"""
    Based on the following report:
    {report_content}
    
    Create 5 multiple-choice questions.
    Each question should have:
    - A question text
    - One correct answer
    
    Format the response as a JSON list where each item contains 'question_text' and 'correct_answer'.
    """
    
    # Get the response from the model
    response = model.invoke(quiz_prompt)
    
    # Check if response is in expected dictionary format
    if isinstance(response, tuple):
        response = response[0]  # Get the dictionary part of the tuple if response is a tuple

    if not isinstance(response, list):
        raise ValueError("Expected response to be a list of dictionaries.")
    
    return response

# Step 2: Add incorrect answers for each question
async def add_incorrect_answers(questions: List[Dict[str, str]]) -> List[Dict[str, Dict[str, str]]]:
    quiz_with_choices = []
    
    for question in questions:
        question_text = question["question_text"]
        correct_answer = question["correct_answer"]
        
        # Prompt to generate three incorrect answers
        incorrect_prompt = f"""
        For the question: "{question_text}"
        The correct answer is: "{correct_answer}"
        
        Generate three plausible but incorrect answer choices.
        
        Format the response as a JSON list of three incorrect answers.
        """
        
        # Get the response from the model
        incorrect_response = model.invoke(incorrect_prompt)

        # Check if response is a tuple and handle it
        if isinstance(incorrect_response, tuple):
            incorrect_response = incorrect_response[0]  # Get the dictionary part if response is a tuple

        if not isinstance(incorrect_response, list) or len(incorrect_response) < 3:
            raise ValueError("Expected response to be a list of three incorrect answers.")
        
        # Organize the question with choices
        question_with_choices = {
            "question_text": question_text,
            "choices": {
                "A": correct_answer,
                "B": incorrect_response[0],
                "C": incorrect_response[1],
                "D": incorrect_response[2]
            },
            "correct_answer": "A"  # Setting 'A' as the correct answer
        }
        
        quiz_with_choices.append(question_with_choices)
    
    return quiz_with_choices

# Main function to generate the quiz
async def generate_quiz():
    # Step 1: Get questions with correct answers
    questions = await generate_questions_with_correct_answers()
    
    # Step 2: Add incorrect answers to each question
    final_quiz = await add_incorrect_answers(questions)
    
    return final_quiz
