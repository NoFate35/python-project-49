import random


def generate_operator():
    operator = random.randint(1, 3)
    match operator:
        case 1:
            return addition()
        case 2:
            return subtraction()
        case 3:
            return multiply()


def addition():
    first_argument = random.randint(1, 50)
    second_argument = random.randint(1, 50)
    return (str(first_argument + second_argument),
            f'{first_argument} + {second_argument}')


def subtraction():
    first_argument = random.randint(65, 100)
    second_argument = random.randint(1, 64)
    return (str(first_argument - second_argument),
            f'{first_argument} - {second_argument}')


def multiply():
    first_argument = random.randint(1, 10)
    second_argument = random.randint(1, 10)
    return (str(first_argument * second_argument),
            f'{first_argument} * {second_argument}')
