import random
import colorama
import sys
from termcolor import colored, cprint

players = []

class cube:
    def __init__ (self, sides):
        self.sides = sides
        
cube.sides = 5000000

player_0 = input('Player one name:  ')
player_1 = input('Player two name:  ')
players.append(player_0)
players.append(player_1)

def game(cube):
    rounds = 0
    while cube.sides != 1:
        print('')
        print(f'Press any button to roll the dice, {player_0}')
        rest = input('')
        cube.sides = random.randint(1, cube.sides)
        print(f"{player_0} roll the dice and gets {cube.sides}")
        if cube.sides == 1:
            print(f'{player_1} winns')
        print('')
        print(f'Press any button to roll the dice, {player_1}')
        rest = input('')
        cube.sides = random.randint(0, cube.sides)
        print(f"{player_1} roll the dice and gets {cube.sides}")
        if cube.sides == 1:
            print(f'{player_0} winns')
        rounds += 1
        text = colored(f"You are now on round {rounds}", 'red', attrs=['reverse', 'blink'])
        print(text)
        
game(cube)