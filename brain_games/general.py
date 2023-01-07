import prompt


def body_games(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.game_rule)
    wrong_answer = 'is wrong answer ;(. Correct answer was'
    i = 1
    while i <= 3:
        question, correct_answer = game.current_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' {wrong_answer} '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            i += 10
        if i == 4:
            print(f'Congratulations, {name}!')
