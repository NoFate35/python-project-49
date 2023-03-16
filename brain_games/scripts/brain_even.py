
from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.even import even_checking


def main():
    game_rules = """Answer "yes" if the number is even,
                    otherwise answer "no"."""
    game_function = even_checking
    body_game_displaying(game_rules, game_function)
