# test_trivia.py

import pytest

from trivia import Question, Quiz
from trivia import run_quiz

run_quiz()

from trivia import Quiz, Question


def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")

def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")


def test_quiz_multiple_questions():
    quiz = Quiz()
    q1 = Question("1 + 1?", ["1", "2", "3", "4"], "2")
    q2 = Question("Capital de Alemania?", ["Madrid", "Berlín", "Lima", "Roma"], "2")
    quiz.add_question(q1)
    quiz.add_question(q2)
    
    assert quiz.answer_question(q1, "2") is True
    assert quiz.answer_question(q2, "1") is False
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 1


def test_quiz_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    quiz.add_question(question)
    assert quiz.answer_question(question, "4") == True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0

    assert quiz.answer_question(question, "2") == False
    assert quiz.incorrect_answers == 1

