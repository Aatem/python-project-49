import prompt


NUMBER_OF_ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
    wrong_answer = 'is wrong answer ;(. Correct answer was'
    i = 1
    while i <= NUMBER_OF_ROUNDS:
        question, correct_answer = game.generate_question_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' {wrong_answer} '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        if i > NUMBER_OF_ROUNDS:
            print(f'Congratulations, {name}!')
