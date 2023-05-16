from colorama import Fore, Style
import os
import http.server
import socketserver
import RSA_keys

hemligt_medelande = []
krypterat_medelande = []
dekrypterat_medelande = []
letters_to_numbers ={
    # Uppercase letters
    'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 'I': 10,
    'J': 11, 'K': 12, 'L': 13, 'M': 14, 'N': 15, 'O': 16, 'P': 17, 'Q': 18,
    'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25, 'Y': 26,
    'Z': 27,
    # Lowercase letters
    'a': 28, 'b': 29, 'c': 30, 'd': 31, 'e': 32, 'f': 33, 'g': 34, 'h': 35,
    'i': 36, 'j': 37, 'k': 38, 'l': 39, 'm': 40, 'n': 41, 'o': 42, 'p': 43,
    'q': 44, 'r': 45, 's': 46, 't': 47, 'u': 48, 'v': 49, 'w': 50, 'x': 51,
    'y': 52, 'z': 53,
    # Swedish characters
    'å': 54, 'ä': 55, 'ö': 56,
    # Punctuation marks
    ',': 57, '.': 58, '/': 59, '?': 60, '!': 61, '-': 62, '_': 63, ':': 64,
    ';': 65, '(': 66, ')': 67, "'": 68, '"': 69, '#': 70, '$': 71, '&': 72,
    '*': 73, '+': 74, '<': 75, '=': 76, '>': 77, '@': 78, '[': 79, ']': 80,
    '^': 81, '`': 82, '{': 83, '|': 84, '}': 85, '~': 86,
    # Digits and other characters
    '0': 87, '1': 88, '2': 89, '3': 90, '4': 91, '5': 92, '6': 93, '7': 94,
    '8': 95, '9': 96, ' ': 99, '\n': 100, '\t': 101, '\r': 102, '½': 103,
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True: 
        p, q, n, phi, e, d = RSA_keys.generate_rsa_keys()
           
        chois = (input("Tryck (1) för att skriva ett medelande\nTryck (2) för att avkryptera medelanden\n:   "))
        print('\n')
        try:
            chois = int(chois)
        except:
            ValueError
            print('Invalid input')
            
        if chois == 1:
            try:
                crypt(e, n)
                de_crypt(d, n)
            except KeyError:
                print('No, somthing in this line of data is not enebled to be convorted into a crypt')
            add_crypt_to_list(d, n)
        elif chois == 2:
            get_crypt_by_index(d,n)
        else:
            pass
        print('\n')
            
def get_crypt_by_index(d,n):
    with open("egna_spel/RSA_Teknik/krypterade_medelande.txt", 'r') as fp:
            max_index = len(fp.readlines())
    print(f'The max index is now ({max_index-1})')
    
    index_to_get = int(input('What index number are you looking for:    '))
    
    #Hittar nycklarna
    
    with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'r') as f:
        for line in f:
            if line.startswith(f"{index_to_get}:"):
                
                crypt_str = line.split(":")[1].strip()
                crypt_numbers = [int(x) for x in crypt_str.split()]
                
                print(f"The incrypted version is {crypt_numbers} \nThe cryptated version is:")
                
                #de crypt 
                dekrypterat_medelande.clear()
                n, d = RSA_keys.tolk_rsa(index_to_get)

                for i in crypt_numbers:
                    dec=pow(i,d,n)
                    for letter, number in letters_to_numbers.items():
                        if number == dec:
                            dekrypterat_medelande.append(letter)
                            
                print(Fore.RED + "".join(map(str, dekrypterat_medelande)) + Style.RESET_ALL)   
    return None

def crypt(e, n):
    
    medelande = input('Skriv ett medelande:     ')
    if medelande == '':
        medelande = 'Blank message'
    hemligt_medelande.clear()
    dekrypterat_medelande.clear()
    krypterat_medelande.clear()
    
    for letter in medelande:
        hemligt_medelande.append(letter)
       
    for i in hemligt_medelande:
        m = letters_to_numbers[i]
        #crypt
        enc=pow(m,e,n)
        crypt_number = (enc)
        krypterat_medelande.append(crypt_number)
    
    with open("egna_spel/RSA_Teknik/krypterade_medelande.txt", 'r') as fp:
        max_index = len(fp.readlines())
        print(f'Your\'e incryption is now stored whit the list index:   {max_index}')

def de_crypt(d, n):
    for i in krypterat_medelande:
        #decrypt
        dec=pow(i,d,n)
        for letter, number in letters_to_numbers.items():
            if number == dec:
                dekrypterat_medelande.append(letter)

def add_crypt_to_list(d, n):
    with open("egna_spel/RSA_Teknik/krypterade_medelande.txt", 'r') as fp:
        max_index = len(fp.readlines())

    with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'a') as f:
        f.write(f"{max_index}: " + ' '.join(map(str, krypterat_medelande)) + f": {n}, {d}" + "\n")

menu()