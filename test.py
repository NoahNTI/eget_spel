vokal_list = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
vokal_amount = []

def main():
    word = input('Type a word:  ')
    for letter in word:
        if letter in vokal_list:
            print(letter)
            vokal_amount.append(letter)
    print(len(vokal_amount))

main()