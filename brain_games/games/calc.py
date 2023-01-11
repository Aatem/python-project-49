import random


GAME_RULE = 'What is the result of the expression?'


def generate_question_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operation = random.choice([' + ', ' - ', ' * '])
    question = str(first_number) + operation + str(second_number)
    if operation == ' + ':
        correct_answer = str(first_number + second_number)
    if operation == ' - ':
        correct_answer = str(first_number - second_number)
    if operation == ' * ':
        correct_answer = str(first_number * second_number)
    return question, correct_answer
