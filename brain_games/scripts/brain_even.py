#!/usr/bin/env python3

from brain_games.game_logic import greeting_user
from brain_games.game_logic import brain_even_logic


def main():

    greeting_user.greeting()
    user_name = greeting_user.welcome_user()
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    result_number_displaying = brain_even_logic.number_displaying()
    if result_number_displaying is True:
        print(f"Congratulations, {user_name}!")
    else:
        user_answer, correct_answer = result_number_displaying
        print(f"'{user_answer}' is wrong answer ;(.")
        print(f"Correct answer was'{correct_answer}'.")
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    main()
