import random
'''generate a random number, check for even and return
(correct answer, random number as question) to round_logic.round_displaying'''


def even_checking():
    number = random.randint(1, 100)
    if number % 2 == 0:
        return ('yes', str(number))
    return ('no', str(number))
