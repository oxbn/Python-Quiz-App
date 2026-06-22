import json
import os
import random

score = 0

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), 'questions.json')

def load_questions():
    with open(QUESTIONS_FILE, 'r') as f:
        return json.load(f)
    
questions_list = list(load_questions().items())
random.shuffle(questions_list)

for question, answer in questions_list:
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}")

percentage = score/len(questions_list) * 100
print(f"You got {score} out of {len(questions_list)} correct. Your score is {percentage:.1f}%.")