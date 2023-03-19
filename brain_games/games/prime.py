#!/usr/bin/env python3
import random


def get_random_number():
    random_number = random.randint(2, 30)
    return (check_for_prime(random_number), str(random_number))


def check_for_prime(random_number):
    divisors_list = list(range(2, random_number))
    for i in divisors_list:
        if random_number % i == 0:
            return 'no'
    return 'yes'


def main():
    get_random_number()


if __name__ == '__main__':
    main()
