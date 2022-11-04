import random
import time

class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


def Fight(Player,Monster):
    time.sleep(0.2)
    while Monster.hp>0:
        fight_1 = input('Vill du slå monstret? I så fall skriv (ja), annars skriv (nej)' ).lower()
        if fight_1 == 'ja':
            Monster.hp -= Player.damage
            print(f'Du slår monstret och dess nya HP är {Monster.hp}')
        elif fight_1 == 'nej':
          print('du e dum')
    
monster_1 = Monster('Monster', 10, 3)
player = Player('pass', 100, 10)

Player.name = input('Hej, vad heter du?:    ')

days = 0
days_end = random.randint(10,15)
print(days_end)

while days != days_end:
    print('')
    Fight(player,monster_1)
    time.sleep(0.2)
    days += 1
    print(days)
    monster_1.hp += 2

    
if days == days_end:
    print('bra jobbat')