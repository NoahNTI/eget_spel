import random
import string
import re

def creat_regg():
    regg = (random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + ' ').upper()
    regg += str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    return regg

def add_regg_to_list():
    new_regg = creat_regg()
    '''with open('egna_spel/regplåt/allowed_regg.txt', 'r') as f:
       while new_regg in f.read():
           new_regg = creat_regg()'''
    
    with open('egna_spel/regplåt/allowed_regg.txt', 'a') as f:
        f.write(new_regg + '\n')

def CUM():
    with open('egna_spel/regplåt/allowed_regg.txt', 'r') as f:
        contents = f.read()
        match = re.search('CUM(?=\s)', contents)
        occurrences = len(re.findall('CUM(?=\s)', contents))
        print(occurrences)


def remove_duplicates():
    with open('egna_spel/regplåt/allowed_regg.txt', 'r') as f:
        contents = f.read().splitlines()
        unique_reggs = []
        for regg in contents:
            if regg not in unique_reggs:
                unique_reggs.append(regg)
    
    with open('egna_spel/regplåt/allowed_regg.txt', 'w') as f:
        for regg in unique_reggs:
            f.write(regg + '\n')

while True:
    add_regg_to_list()

