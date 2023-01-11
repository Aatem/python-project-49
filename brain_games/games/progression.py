import random


GAME_RULE = 'What number is missing in the progression?'


def generate_question_answer():
    length = random.randint(5, 10)
    step = random.randint(1, 10)
    first_number = random.randint(1, 10)
    number = random.randint(0, length - 1)
    i = 1
    s = [first_number]
    while i <= length - 1:
        s.append(s[i - 1] + step)
        i += 1
    correct_answer = str(s[number])
    s[number] = '..'
    question = ' '.join([str(value) for value in s])
    return question, correct_answer
