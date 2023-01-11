import random
from math import sqrt


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = random.randint(1, 20)
    question = number
    correct_answer = 'yes'
    if number <= 1:
        correct_answer = 'no'
    else:
        i = 2
        while i <= sqrt(number):
            if number % i == 0:
                correct_answer = 'no'
                break
            i += 1
    return question, correct_answer
