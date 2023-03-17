import random


def get_random_numbers_for_gcd():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    if number1 >= number2:
        first_number = number1
        second_number = number2
    else:
        first_number = number2
        second_number = number1
    return (get_divisors_lists(first_number, second_number),
            f'{number1} {number2}')


def get_divisors_lists(first_number, second_number):
    first_number_divisors = []
    for i in range(1, first_number + 1):
        if first_number % i == 0:
            first_number_divisors.append(i)
    second_number_divisors = []
    for i in range(1, second_number + 1):
        if second_number % i == 0:
            second_number_divisors.append(i)
    return get_gcd(first_number_divisors, second_number_divisors, )


def get_gcd(first_number_divisors, second_number_divisors):
    first_number_divisors.sort(reverse=True)
    second_number_divisors.sort(reverse=True)
    for i in second_number_divisors:
        if i in first_number_divisors:
            return str(i)


def main():
    get_random_numbers_for_gcd()


if __name__ == '__main__':
    main()
