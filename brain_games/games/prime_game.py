from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def find_prime(random_number):
    if random_number == 1:
        return False
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            return False
    return True


def get_game():
    question = randint(1, 100)
    random_number = question
    if find_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
