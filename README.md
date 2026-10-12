# ExamPrep — Python Quiz Application

ExamPrep is a command-line quiz application built with Python. It presents multiple-choice questions, checks answers, calculates the final score, assigns a grade, and saves test results to a CSV file.

## Features

* Multiple-choice questions with A, B, C, and D options
* Input validation for user answers
* Automatic score calculation in percentages
* Grade feedback based on the final score
* Questions loaded from a JSON file
* Results saved to `results.csv`
* Automated tests using pytest

## Technologies

* Python
* JSON
* CSV
* pytest

## Project Structure

* `project.py` — main application and quiz logic
* `questions.json` — quiz questions and correct answers
* `test_project.py` — automated tests
* `results.csv` — saved quiz results (created after completing a quiz)
* `requirements.txt` — project dependencies

## How to Run

1. Install Python 3.14 or a compatible Python version.

2. Open a terminal in the project directory.

3. Run the application:

   `python project.py`

4. Choose **1** to start a quiz or **2** to exit.

## Run Tests

Install pytest:

`python -m pip install pytest`

Run the tests:

`python -m pytest test_project.py -v`

## How Scoring Works

The application calculates the percentage of correct answers using:

`score = correct_answers / total_questions * 100`

It then provides feedback based on the final percentage and stores the result with the date and time.

## Purpose

This project was created to practise Python functions, loops, conditional statements, file handling, JSON parsing, CSV writing, input validation, and automated testing.
## 🎥 Project Demo

Watch the ExamPrep final project presentation on YouTube:

[**ExamPrep — CS50P Final Project | Bobur Komiljonov**](https://youtu.be/ia7aKSJOGE4)

# maratesbot
