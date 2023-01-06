import random


game_rule = 'Find the greatest common divisor of given numbers.'


def current_game():
    first_ramdom_number = random.randint(1, 100)
    second_random_number = random.randint(1, 100)
    question = str(first_ramdom_number) + ' ' + str(second_random_number)
    while first_ramdom_number != 0 and second_random_number != 0:
        if first_ramdom_number > second_random_number:
            first_ramdom_number = first_ramdom_number % second_random_number
        else:
            second_random_number = second_random_number % first_ramdom_number
    correct_answer = str(first_ramdom_number + second_random_number)
    return question, correct_answer
