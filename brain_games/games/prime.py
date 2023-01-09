from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def find_prime(number):
    if number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def game_body():
    question = randint(1, 100)
    number = question
    if find_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
