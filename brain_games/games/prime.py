import random


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def current_game():
    random_number = random.randint(1, 20)
    question = random_number
    correct_answer = 'yes'
    if random_number <= 1:
        correct_answer = 'no'
    else:
        i = 2
        while i <= sqrt(random_number):
            if random_number % i == 0:
                correct_answer = 'no'
                break
            i += 1
    return question, correct_answer
