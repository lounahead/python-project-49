from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_body():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer
