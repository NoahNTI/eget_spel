from colorama import Fore, Style

hemligt_medelande = []
krypterat_medelande = []
dekrypterat_medelande = []

letters_to_numbers = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5,
    'E': 6,
    'F': 7,
    'G': 8,
    'H': 9,
    'I': 10,
    'J': 11,
    'K': 12,
    'L': 13,
    'M': 14,
    'N': 15,
    'O': 16,
    'P': 17,
    'Q': 18,
    'R': 19,
    'S': 20,
    'T': 21,
    'U': 22,
    'V': 23,
    'W': 24,
    'X': 25,
    'Y': 26,
    'Z': 27,
    'a': 28,
    'b': 29,
    'c': 30,
    'd': 31,
    'e': 32,
    'f': 33,
    'g': 34,
    'h': 35,
    'i': 36,
    'j': 37,
    'k': 38,
    'l': 39,
    'm': 40,
    'n': 41,
    'o': 42,
    'p': 43,
    'q': 44,
    'r': 45,
    's': 46,
    't': 47,
    'u': 48,
    'v': 49,
    'w': 50,
    'x': 51,
    'y': 52,
    'z': 53,
    'å': 54,
    'ä': 55,
    'ö': 56,
    ',': 57,
    '.': 58,
    '/': 59,
    '?': 60,
    '!': 61,
    '-': 62,
    '_': 63,
    ':': 64,
    ';': 65,
    '(': 66,
    ')': 67,
    '0': 68,
    '1': 69,
    '2': 70,
    '3': 71,
    '4': 72,
    '5': 73,
    '6': 74,
    '7': 75,
    '8': 76,
    '9': 77,
    "'": 78,
    '%': 79,
    ' ': 99,
}

p = 1009
q = 2003
n = p*q
phi=(p-1)*(q-1)
e = 1009037
d = 730661

def menu():
    while True:
        chois = int(input("Tryck (1) för att skriva ett medelande\nTryck (2) för att avkryptera medelanden\n:   "))
        if chois == 1:
            try:
                crypt()
                de_crypt()
            except KeyError:
                print('No, somthing in this line of data is not enebled to be convorted into a crypt')
            add_crypt_to_list()
        elif chois == 2:
            get_crypt_by_index()
            
def get_crypt_by_index():
    index_to_get = int(input('What index number are you looking for:    '))
    with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'r') as f:
        for line in f:
            if line.startswith(f"{index_to_get}:"):
                
                crypt_str = line.split(":")[1].strip()
                crypt_numbers = [int(x) for x in crypt_str.split()]
                
                print(f"The incrypted version is {crypt_numbers} \nThe cryptated version is:")
                
                #de crypt 
                dekrypterat_medelande.clear()
                for i in crypt_numbers:
                    dec=pow(i,d,n)
                    for letter, number in letters_to_numbers.items():
                        if number == dec:
                            dekrypterat_medelande.append(letter)
                print(Fore.RED + "".join(map(str, dekrypterat_medelande)) + Style.RESET_ALL)   
                print('\n')              
    return None

def crypt():
    medelande = input('Skriv ett medelande:     ')
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

def de_crypt():
    for i in krypterat_medelande:
        #decrypt
        dec=pow(i,d,n)
        anti_krypt = (dec,d,n)
        for letter, number in letters_to_numbers.items():
            if number == dec:
                dekrypterat_medelande.append(letter)
                
def add_crypt_to_list():
    with open("egna_spel/RSA_Teknik/krypterade_medelande.txt", 'r') as fp:
        max_index = len(fp.readlines())
    
    with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'a') as f:
        f.write(f"{max_index}: " + ' '.join(map(str, krypterat_medelande)) + "\n")

while True:
    menu()
    
    """""
    crypt()
    de_crypt()
    print(*krypterat_medelande)
    add_crypt_to_list()
    get_crypt_by_index()
    """
    
    
    print(krypterat_medelande)
    print(dekrypterat_medelande)
    print()