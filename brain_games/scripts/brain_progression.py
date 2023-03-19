#!/usr/bin/env python3
from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.progression import get_progression

'''Send rules of the game and function of the game into 'body_game_displaying'''


def main():
    game_rules = "What number is missing in the progression?"
    game_function = get_progression
    body_game_displaying(game_rules, game_function)


if __name__ == '__main__':
    main()
