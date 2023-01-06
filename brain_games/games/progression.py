import random


game_rule = 'What number is missing in the progression?'


def current_game():
    random_length = random.randint(5, 10)
    random_step = random.randint(1, 10)
    random_first_number = random.randint(1, 10)
    random_number = random.randint(0, random_length - 1)
    i = 1
    s = [random_first_number]
    while i <= random_length - 1:
        s.append(s[i - 1] + random_step)
        i += 1
    correct_answer = str(s[random_number])
    s[random_number] = '..'
    string = ''
    for symbol in s:
        string = string + str(symbol) + ' '
    question = string.strip()
    return question, correct_answer
