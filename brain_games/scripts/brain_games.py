#!/usr/bin/env python3

import  brain_games.cli

def greeting():
	print('Welcome to the Brain Games!')



def main():
	greeting()
	brain_games.cli.welcome_user()

if __name__ == '__main__':
	main()
