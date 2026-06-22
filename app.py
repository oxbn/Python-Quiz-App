import json
import os
import random

score = 0
questions_answered = 0
missed_questions = []

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), 'questions.json')

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

def ask_questions(question):
    if question['type'] == 0:
        user_answer = input(f"{question['question']} ")
        correct_answer = question['answer']

    else:
        print(question['question'])
        print("Options: ")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        user_answer = input("> ")
        if user_answer.isdigit():
            choice = int(user_answer)

            if 1 <= choice <= len(question['options']):
                user_answer = question['options'][choice - 1]
            else:
                print("Please enter a valid option number.")
                return ask_questions(question)
            
        correct_answer = question['options'][question['correctAnswer']]

    return user_answer, correct_answer

with open(QUESTIONS_FILE, "r") as file:
    data = json.load(file)

random.shuffle(data["questions"])

for q in data["questions"]:
    user_answer, correct_answer = ask_questions(q)

    if user_answer.strip().lower() == "quit":
        print("Exiting the quiz.")
        break

    questions_answered += 1

    if check_answer(user_answer, correct_answer):
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")
        missed_questions.append((q["question"], correct_answer))

percentage = score/questions_answered * 100 if questions_answered > 0 else 0
print(f"You got {score} out of {questions_answered} correct. Your score is {percentage:.1f}%.")

if missed_questions:
    print("\nQuestions you got wrong:")
    for question, answer in missed_questions:
        print(f"- {question}: {answer}")