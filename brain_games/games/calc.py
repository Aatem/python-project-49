import random


game_rule = 'What is the result of the expression?'


def current_game():
    fir_ramdom_number = random.randint(1, 100)
    sec_random_number = random.randint(1, 100)
    random_symbol = random.choice([' + ', ' - ', ' * '])
    question = str(fir_ramdom_number) + random_symbol + str(sec_random_number)
    if random_symbol == ' + ':
        correct_answer = str(fir_ramdom_number + sec_random_number)
    if random_symbol == ' - ':
        correct_answer = str(fir_ramdom_number - sec_random_number)
    if random_symbol == ' * ':
        correct_answer = str(fir_ramdom_number * sec_random_number)
    return question, correct_answer
