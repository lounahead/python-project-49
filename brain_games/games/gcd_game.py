import math
from random import randint
RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    question = f'{random_num1} {random_num2}'
    correct_answer = str(math.gcd(random_num1, random_num2))
    return question, correct_answer
