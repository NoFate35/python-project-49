from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.progression import get_progression


def main():
    game_rules = "What number is missing in the progression?"
    game_function = get_progression
    body_game_displaying(game_rules, game_function)
