#!/usr/bin/env python3
from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.calc import generate_operator

'''Send rules of the game and function of the game into 'body_game_displaying'''


def main():
    game_rules = "What is the result of the expression?"
    game_function = generate_operator
    body_game_displaying(game_rules, game_function)


if __name__ == '__main__':
    main()
