from random import randint
import random
RULE = 'What is the result of the expression?'


def game_body():
    operators = ['-', '+', '*']
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    if operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '+':
        correct_answer = num1 + num2
    return question, str(correct_answer)
