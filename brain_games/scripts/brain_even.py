#!/usr/bin/env python3
from brain_games.game_logics.body_game_logic import body_game_displaying
from brain_games.games.even import even_checking

'''Send rules of the game and function of the game into 'body_game_displaying'''


def main():
    game_rules = ('''Answer "yes" if the number is even, '''
                  '''otherwise answer "no".''')
    game_function = even_checking
    body_game_displaying(game_rules, game_function)


if __name__ == '__main__':
    main()
