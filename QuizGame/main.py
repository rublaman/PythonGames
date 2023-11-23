from QuizGame.data import question_data
from QuizGame.question_model import Question
from QuizGame.quiz_brain import QuizBrain

question_bank = []


def run_quiz():
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_question():
        quiz.next_question()

def start():
    run_quiz()