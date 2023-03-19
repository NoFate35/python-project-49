from brain_games.game_logics import greeting_user
from brain_games.game_logics import round_logic

'''This function:
1. greeting user
2. get user name
3. print game rules
3. call the round function and transmits to it game
    function (recived from script 'brain-....')
4. in depending of user answer - launch Congratulations or Wrong answer '''


def body_game_displaying(game_rules, game_function):

    greeting_user.greeting()
    user_name = greeting_user.welcome_user()
    print(game_rules)
    result_round_displaying = round_logic.round_displaying(game_function)
    if result_round_displaying is True:
        print(f"Congratulations, {user_name}!")
    else:
        user_answer, correct_answer = result_round_displaying
        print(f"'{user_answer}' is wrong answer ;(.", end=' ')
        print(f"Correct answer was'{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
