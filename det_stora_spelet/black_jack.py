import random
import time
import os

cards = []
colors = ['❤', '♣', '♦', '♠']
player_cards = []
player_1_score = []
player_2_score = []
player_cards_display = {'value': 0,
                        'name': 0}

for color in colors:
    cards.append({'name': 'A' + color, 'points': 1})
    cards.append({'name': 'K' + color, 'points': 10})
    cards.append({'name': 'Q' + color, 'points': 10})
    cards.append({'name': 'J' + color, 'points': 10})

    for x in range(2, 11):
        cards.append({'name': str(x) + color, 'points': x})


def card_stats():
    card = random.choice(cards)
    cards.remove(card)
    player_cards.append(card)
    return card['name'], card['points']


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_card():
    print(" _____ ")
    print("|{}   |".format(player_cards_display["points"]))
    print("| {} |".format(player_cards_display["name"]))
    print("|   {}|".format(player_cards_display["points"]))
    print(" ‾‾‾‾‾ ")


def player_game_1():
    print('player (1) can now start to play')
    time.sleep(2)
    clear()

    score_p_1 = 0
    card_name, card_points = card_stats()
    player_cards_display['name'] = card_name
    player_cards_display['points'] = card_points
    score_p_1 = card_points

    print(
        f'Your first card is {card_name} and you now have {score_p_1} points')
    display_card()
    while True:
        choice_1 = input('Do you want a new card (Y/N): ').lower()
        if choice_1 == 'n':
            print(f'Your score is {21-score_p_1} from 21')
            break

        elif choice_1 == 'y':
            card_name, card_points = card_stats()

            player_cards_display['name'] = card_name
            player_cards_display['points'] = card_points
            display_card()

            score_p_1 += card_points
            if score_p_1 > 21:
                print(f'Your now above 21 whit a score of {score_p_1}')
                score_p_1 = 0
                break
            else:
                print(
                    f'Your new card is {card_name} and you now have {score_p_1} points')
    player_1_score.append(score_p_1)


def player_game_2():
    print('player (2) can now start to play')
    time.sleep(2)
    clear()

    score_p_2 = 0
    card_name, card_points = card_stats()

    player_cards_display['name'] = card_name
    player_cards_display['points'] = card_points

    score_p_2 = card_points
    print(
        f'Your first card is {card_name} and you now have {score_p_2} points')
    display_card()
    while True:
        choice_1 = input('Do you want a new card (Y/N): ').lower()
        if choice_1 == 'n':
            print(f'Your score is {21-score_p_2} from 21')
            break

        elif choice_1 == 'y':
            card_name, card_points = card_stats()

            player_cards_display['name'] = card_name
            player_cards_display['points'] = card_points
            display_card()

            score_p_2 += card_points
            if score_p_2 > 21:
                print(f'Your now above 21 whit a score of {score_p_2}')
                score_p_2 = 0
                break
            else:
                print(
                    f'Your new card is {card_name} and you now have {score_p_2} points')
    player_2_score.append(score_p_2)


def who_winns():
    score_1 = player_1_score[0]
    score_2 = player_2_score[0]
    if score_1 == score_2:
        print('The game is a draw')
    elif score_1 > score_2:
        print(f'player (1) winns by being {21-score_1} away from 21')
    elif score_2 > score_1:
        print(f'player (2) winns by being {21-score_2} away from 21')


def game():
    player_game_1()
    time.sleep(1)
    clear()
    player_game_2()
    clear()
    who_winns()


game()
