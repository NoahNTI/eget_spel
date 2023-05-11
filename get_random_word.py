import random
import codecs

# file = open("egna_spel/ordlista.txt", "r", "utf-8")
def word():
    file = codecs.open("egna_spel/ordlista.txt", "r", "utf-8")
    words = file.read().splitlines()
    word = random.choice(words)
    return str(word)
