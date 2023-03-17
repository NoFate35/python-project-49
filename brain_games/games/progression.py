import random


def get_progression():
    progression_start = random.randint(1, 30)
    progression_len = random.randint(5, 10)
    progression_step = random.randint(1, 5)
    progression = list(range(progression_start,
                       progression_start + progression_len * progression_step,
                       progression_step))
    missing_element_position = random.randint(0, progression_len - 1)
    missing_element = progression.pop(missing_element_position)
    progression.insert(missing_element_position, '..')
    str_progression = [str(i) for i in progression]
    # print((str(missing_element), ' '.join(str_progression)))
    return (str(missing_element), ' '.join(str_progression))


def main():
    get_progression()


if __name__ == '__main__':
    main()
