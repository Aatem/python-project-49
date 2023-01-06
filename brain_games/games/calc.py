import random


game_rule = 'What is the result of the expression?'


def current_game():
    first_ramdom_number = random.randint(1, 100)
    second_random_number = random.randint(1, 100)
    random_symbol = random.choice([' + ', ' - ', ' * '])
    question = str(first_ramdom_number) + random_symbol + str(second_random_number)
    if random_symbol == ' + ':
        correct_answer = str(first_ramdom_number + second_random_number)
    if random_symbol == ' - ':
        correct_answer = str(first_ramdom_number - second_random_number)
    if random_symbol == ' * ':
        correct_answer = str(first_ramdom_number * second_random_number)
    return question, correct_answer
