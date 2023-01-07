import random


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def current_game():
    random_number = random.randint(1, 20)
    question = random_number
    k = 0
    for i in range(2, (random_number // 2) + 3):
        if random_number % i == 0:
            k += 1
        if k == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    if random_number == 1:
        correct_answer = 'no'
    return question, correct_answer
