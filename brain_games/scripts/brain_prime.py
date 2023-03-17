from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.prime import get_random_number

'''Send rules of the game and function of the game into 'body_game_displaying'''


def main():
    game_rules = "Answer 'yes' if given number is prime.Otherwise answer 'no'."
    game_function = get_random_number
    body_game_displaying(game_rules, game_function)
