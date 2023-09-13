import random
import time
import os
import get_random_word


letters = []
word_word_3 = []
ncorrect_letters = []
letter_used = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def guess():
    wrong_guesses = 0
    while '_' in word_word_3:
        print(" ".join(word_word_3))
        print('')
        print('What letter do you think is in the word?: ')
        letter_guess = input('').upper()
        if letter_guess == None:
            print('That\'s not a letter')
        elif letter_guess in letter_used:
            print('You have alredy guesst that word')
        elif letter_guess == '_':
            print('No can do')
        else:
            if letter_guess in ncorrect_letters:
                print("You have allredy guesst that letter")
                wrong_guesses += 1
                print(f'you have {13 - wrong_guesses} guesses left')
                if 13 - wrong_guesses == 0:
                    print(word_word_3)
                    break
            elif letter_guess in letters:
                letter_in_word(letter_guess)
                ncorrect_letters.append(letter_guess)
            else:
                print("No, that's not in the word")
                wrong_guesses += 1
                print(f'you have {13 - wrong_guesses} guesses left')
            letter_used.append(letter_guess)
        print('\n\n\n\n\n')


def letter_in_word(letter_guess):
    i = 0
    for letter in letters:
        if letter_guess == letters[i]:
            word_word_3[i] = letter_guess
        i += 1


word = str(get_random_word.word()).upper()
clear()

for letter in word:
    letters.append(letter)
for x in letters:
    if x == ' ':
        word_word_3.append(' ')
    else:
        word_word_3.append('_')

while True:
    guess()
    print(f'Great jobb, you word whas {" ".join(word_word_3)}')
    break
