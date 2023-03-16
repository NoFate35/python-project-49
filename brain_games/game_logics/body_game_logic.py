from brain_games.game_logics import greeting_user
from brain_games.game_logics import round_logic


def body_game_displaying(game_rules, game_function):

    greeting_user.greeting()
    user_name = greeting_user.welcome_user()
    print(game_rules)
    result_round_displaying = round_logic.round_displaying(game_function)
    if result_round_displaying is True:
        print(f"Congratulations, {user_name}!")
    else:
        user_answer, correct_answer = result_round_displaying
        print(f"'{user_answer}' is wrong answer ;(.")
        print(f"Correct answer was'{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
