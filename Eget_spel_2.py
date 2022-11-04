import random
import time
import os

class player:
    def __init__(self,name, damage, speed, hp, luck, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.luck = luck
        self.armor = armor
        hp = hp + armor

class inventory:
    def __init__(self, coin ,healing_potion, attack_potion, armor):
        self.coin = coin
        self.healing_potion = healing_potion
        self.attack_potion = attack_potion
        self.armor = armor

def wait():
    time.sleep(0.4)
    print('-\n')
    time.sleep(0.4)
    print('-\n')
    time.sleep(0.4)
    print('-\n')
    time.sleep(0.4)
    time.sleep(0.4)
    print('-\n')

def healing_potion(player, inventory):
    if inventory.healing_potion == 0:
        print('Det går inte då du inte har några')
    else:
        inventory.healing_potion = inventory.healing_potion - 1
        player.hp = player.hp + 50
        print (f'Du får 50 mera HP och har nu {player.hp} HP')

def attack_potion(player, inventory):
    if inventory.attack_potion == 0:
        print('Det går inte då du inte har några')
    else:
        inventory.attack_potion = inventory.attack_potion - 1
        player.damage = player.damage + 10
        print (f'Du får 10 mera attack förmåga och har nu {player.damage} i skada')

class monster:
    def __init__(self,name,hp,damage,agro,count):
        self.count = count
        self.name = name
        self.hp = hp
        self.damage = damage
        self.agro = agro

'''monster list'''
monster = monster(monster, random.randint(100,130), random.randint(7,15), random.randint(1,6), 1)


'''def fight_scenario_1(player, monster):
    print(f'Medan du går stöter du på ett monster med namnet {monster.name} och har {monster.hp} i HP')
    #print(f'Innan du hinner reagera slår {monster.name} dig och gör {monster.damage} skada på dig, ditt nya HP är nu {player.hp - monster.damage}')
    while not monster.hp <= 0:
        crit_hit = random.randint(1,4) - player.luck
        if crit_hit<=0:
            crit_hit=1
        monster_attack = random.randint(1,3) 
        act_1 = int(input('Tryck (1) för att attackera eller tryck (2) för att inte göra något alls \n:  '))
        if act_1 == 1:
            monster.hp = monster.hp - player.damage
            if monster.hp <= 0:
                print('Bra jobbat du dödade monstret, du får nu gå vidare')
                coin_loot = random.randint(8, 17)
                inventory.coin = inventory.coin + coin_loot
                print(f'Du går förbi liket av monstret och hittar {coin_loot} stycken coins')
                break
            elif monster.hp >0 and crit_hit==1:
                monster.hp = monster.hp-player.damage*2
                if monster.hp-player.damage*2 <=0:
                    print('Bra du dödade monstret')
                    coin_loot = random.randint(8, 17)
                    inventory.coin = inventory.coin + coin_loot
                    print(f'Du går förbi liket av monstret och hittar {coin_loot} stycken coins')
                    break
                else:    
                    print (f'Du attackerar monstret med en attack boost, dess nya HP är {monster.hp}')
            elif monster.hp >0:
                print (f'du attackerar monstret, dess nya HP är {monster.hp}')
            if monster_attack==1:
                player.hp=player.hp-monster.damage
                if player.hp <= 0:
                    print('Tyvär så slår monstret tillbaka och du dör')
                    exit()
                else:
                    print(f'Medan du attackerar monstret slår det tillbaka och gör {monster.damage} i skada. Ditt nya HP är {player.hp}')
                
        elif act_1 == 2:
            player.hp = player.hp - monster.damage
            if player.hp <= 0:
                    print('Du dog')
                    exit()
            else:
                print(f'Medan du står och pillar dig i naveln så slår monstret dig. Ditt nya HP är {player.hp}')'''
def fight_scenario_2(player, monster):
    print(f'Medan du går stöter du på ett monster med namnet {monster.name} och har {monster.hp} i HP')
    #print(f'Innan du hinner reagera slår {monster.name} dig och gör {monster.damage} skada på dig, ditt nya HP är nu {player.hp - monster.damage}')
    while not monster.hp <= 0:
        crit_hit = random.randint(1,4) - player.luck
        if crit_hit<=0:
            crit_hit=1
        monster_attack = random.randint(1,3) 
        act_1 = int(input('Tryck (1) för att attackera eller tryck (2) för att inte göra något alls\nDu kan även trycka på (3) för att använda dina potions:  '))
        time.sleep(0.3)
        print('')
        if act_1 == 1:
            monster.hp = monster.hp - player.damage
            if monster.hp <= 0:
                print('Bra jobbat du dödade monstret, du får nu gå vidare')
                coin_loot = random.randint(15, 20)
                inventory.coin = inventory.coin + coin_loot
                print(f'Du går förbi liket av monstret och hittar {coin_loot} stycken coins')
                break
            elif monster.hp >0 and crit_hit==1:
                monster.hp = monster.hp-player.damage*2
                if monster.hp-player.damage*2 <=0:
                    print('Bra du dödade monstret')
                    coin_loot = random.randint(8, 17)
                    inventory.coin = inventory.coin + coin_loot
                    print(f'Du går förbi liket av monstret och hittar {coin_loot} stycken coins')
                    monster.count += 1
                    break
                else:    
                    print (f'Du attackerar monstret med en attack boost, dess nya HP är {monster.hp}')
            elif monster.hp >0:
                print (f'du attackerar monstret, dess nya HP är {monster.hp}')
            if monster_attack==1 or monster_attack==2:
                player.hp=player.hp-monster.damage-15
                if player.hp <= 0:
                    print('Tyvär så slår monstret tillbaka och du dör')
                    exit()
                else:
                    print(f'Medan du attackerar monstret slår det tillbaka och gör {monster.damage} i skada. Ditt nya HP är {player.hp}')
                
        elif act_1 == 2:
            player.hp = player.hp - monster.damage
            if player.hp <= 0:
                    print('Du dog')
                    exit()
            else:
                print(f'Medan du står och pillar dig i naveln så slår monstret dig. Ditt nya HP är {player.hp}')
        
        elif act_1 == 3:
            print(f'Okej, du har {inventory.healing_potion} healingpotions och {inventory.attack_potion} attack potions kvar')
            prep_fight = int(input('Tryck (1) för att använda healing potions, (2) för att använda en attack potions eller tryck(9) för att gå tillbaka till fighten\n: '))
            if prep_fight == 1:
                healing_potion(player, inventory)
            elif prep_fight ==2:
                attack_potion(player, inventory)
            else:
                ('Okej')
        
        elif act_1 == 9:
            shop(player, inventory)            
def shop(player, inventory):
    print('Välkomen till shoppen, här kan du köpa saker för att bättra din prestation under strider')
    healing_potion_x = random.randint(1,3)
    while True:
        print('')
        shop_act_1 = int(input('''Tryck (1) för att köpa en healing potion, (2) för att köpa attack potion,
(3) för att köpa armor, (8) för att kolla hur många Coins du har kvar eller (9) för att lämna shoppen: '''))
        print('')
        
        if shop_act_1 == 9:
            print('Okej, då lämnar du shoppen')
        elif shop_act_1 == 8:
            print(f'Du har {inventory.coin} styckens coins kvar')
        elif shop_act_1 == 1:
            shop_act_2 = int(input('Du kan köpa 1 healing potion för 6 coins genom att trycka (1), eller tryck (2) för att avbryta köp\n:'))
            if shop_act_2 ==1:
                if inventory.coin-6<0:
                    print('\nDu har tyvärr inte råd\n')
            else:
                    inventory.coin = inventory.coin - 6
                    inventory.healing_potion = inventory.healing_potion + 1
                    print(f'Bra köp, du har nu {inventory.healing_potion} stycken healing potions')
            if shop_act_2 == 2:
                print('Okej')
        elif shop_act_1 == 2:
            shop_act_2 = int(input('Du kan köpa 1 attack potion för 15 coins genom att trycka (1), eller tryck (2) för att avbryta köp\n:'))
            if shop_act_2 ==1:
                if inventory.coin-15<0:
                    print('\nDu har tyvär inte råd\n')
                else:
                    inventory.coin = inventory.coin - 15
                    inventory.attack_potion = inventory.attack_potion + 1
                    print(f'Bra köp, du har nu {inventory.attack_potion} stycken attack potions')
            if shop_act_2 ==2:
                print('Okej')
        elif shop_act_1 == 3:
            print('Du får inte köpa, jag orkar inte göra den funktionen')
        elif shop_act_1 == 9:
            break

                     
wait()

'''Intro'''

player.name = input('Vad heter du?: ')
'''player.hp = 100
player.armor = 0
player.luck = 0
'''
player = player(player.name, 1, 0, 100, 1, 0)

inventory.coin = 0
inventory.healing_potion = 0
inventory.attack_potion = 0     
inventory.armor = 0

print ('Här är en lista på det vapen du kan välja mellan')
print('Yxa(1)\nSvärd(2)\nNuke(3)\nFist(4)\nKnife(5)\nPistol(6)')
vapen = int(input('Skriv den siffra för det vapen du vill ha\n: '))

if vapen == 1:
    player.damage = 15
    player.speed = 4
elif vapen == 2:
    player.damage = 10
    player.speed = 9
elif vapen == 3:
    player.damage = 123456789
    player.speed = 1
    print('nej')
    time.sleep(1)
    os.system("taskkill /f /im code.exe")
elif vapen == 4:
    player.damage = 1
    player.speed = 20
elif vapen == 5:
    player.damage = 9
    player.speed = 9
elif vapen == 6:
    player.damage = 15
    player.speed = 15
else:
    exit()

print(f'Hej {player.name}! Ditt totala liv är {player.hp} och vid varje attack kommer du göra {player.damage} i skada')

