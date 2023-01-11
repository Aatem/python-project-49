import random


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = str(first_number) + ' ' + str(second_number)
    correct_answer = greatest_common_divisor(first_number, second_number)
    return question, correct_answer


def greatest_common_divisor(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
        result = number_1 + number_2
    return str(result)
