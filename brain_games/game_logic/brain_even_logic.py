#!/usr/bin/env python3

from random import randint
import prompt


def number_displaying():
    question_count = 0
    while question_count < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = number_even_checking(random_number)
        if user_answer != correct_answer:
            return (user_answer, correct_answer)
        print('Correct!')
        question_count += 1
    return True


def number_even_checking(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def main():
    number_displaying()


if __name__ == "__name__":
    main()
