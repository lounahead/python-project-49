from random import randint, choice
RULE = 'What is the result of the expression?'
OPERATORS = ['-', '+', '*']


def get_game():
    random_num1 = randint(1, 10)
    random_num2 = randint(1, 10)
    operator = choice(OPERATORS)
    question = f"{random_num1} {operator} {random_num2}"
    return question, str(get_score(operator, random_num1, random_num2))


def get_score(operator, random_num1, random_num2):
    if operator == '-':
        correct_answer = random_num1 - random_num2
    elif operator == '*':
        correct_answer = random_num1 * random_num2
    elif operator == '+':
        correct_answer = random_num1 + random_num2
    return correct_answer
