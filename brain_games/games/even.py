import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    number = random.randint(1, 100)
    question = number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
