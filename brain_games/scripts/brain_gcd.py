from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.gcd import get_random_numbers_for_gcd


def main():
    game_rules = "Find the greatest common divisor of given numbers."
    game_function = get_random_numbers_for_gcd
    body_game_displaying(game_rules, game_function)
