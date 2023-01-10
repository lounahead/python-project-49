from random import randint
RULE = 'What number is missing in the progression?'


def get_game():
    end_prog = randint(50, 60)
    step_prog = randint(1, 5)
    result = list(range(randint(1, 9), end_prog, step_prog))[:10]
    random_index = randint(0, len(result) - 1)
    correct_answer = result[random_index]
    result[random_index] = '..'
    question = ''
    for i in range(len(result)):
        question = question + str(result[i]) + ' '
    return question, str(correct_answer)
