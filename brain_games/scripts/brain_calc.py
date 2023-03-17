from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.calc import generate_operator


def main():
    game_rules = "What is the result of the expression?"
    game_function = generate_operator
    body_game_displaying(game_rules, game_function)
