import json
import os
import random
from flask import Flask, jsonify, render_template, request #type: ignore

app = Flask(__name__)


def load_questions():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'questions.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


@app.route('/')
def load_json():
    try:
        data = load_questions()
        return render_template('index.html', data=data)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = load_questions()
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

    questions = data['questions']
    results = []
    score = 0

    for i, q in enumerate(questions, start=1):
        submitted = request.form.get(f'q{i}', '')

        if q['type'] == 0:
            correct_answer = q['answer']
            is_correct = submitted.strip().lower() == correct_answer.strip().lower()
        else:
            correct_index = q['correctAnswer']
            is_correct = submitted.isdigit() and int(submitted) == correct_index
            submitted = q['options'][int(submitted)] if submitted.isdigit() else '(no answer)'
            correct_answer = q['options'][correct_index]

        if is_correct:
            score += 1

        results.append({
            'question': q['question'],
            'submitted': submitted,
            'correct_answer': correct_answer,
            'is_correct': is_correct,
        })

    percentage = round(score / len(questions) * 100, 1) if questions else 0
    return render_template('results.html', results=results, score=score,
                           total=len(questions), percentage=percentage)


app.run(debug=True)