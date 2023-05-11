hemligt_medelande = []
krypterat_medelande = []
dekrypterat_medelande = []

letters_to_numbers = {
    'a': 2,
    'b': 3,
    'c': 4,
    'd': 5,
    'e': 6,
    'f': 7,
    'g': 8,
    'h': 9,
    'i': 10,
    'j': 11,
    'k': 12,
    'l': 13,
    'm': 14,
    'n': 15,
    'o': 16,
    'p': 17,
    'q': 18,
    'r': 19,
    's': 20,
    't': 21,
    'u': 22,
    'v': 23,
    'w': 24,
    'x': 25,
    'y': 26,
    'z': 27,
    'å': 28,
    'ä': 29,
    'ö': 30,
    ',': 31,'.': 32,
    '/': 33,'?': 34,
    '!': 35, '-': 36,
    '_': 37, ':': 38,
    ';': 39,'(': 40,
    ')': 41, '0': 42,
    '1': 43, '2': 44,
    '3': 45, '4': 46,
    '5': 47, '6': 48,
    '7': 49, '8': 50,
    '9': 51, "'": 52,
    '%': 53, ' ': 99,
    
}

p = 1009
q = 2003
n = p*q
phi=(p-1)*(q-1)
e = 1009037
d = 730661
index = 1

def get_crypt_by_index():
    index_to_get = int(input('What index number are you looking for:    '))
    with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'r') as f:
        for line in f:
            if line.startswith(f"{index_to_get}:"):
                
                crypt_str = line.split(":")[1].strip()
                crypt_numbers = [int(x) for x in crypt_str.split()]
                print(crypt_numbers)
    return None

def crypt():
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
                
max_index = 0
def add_crypt_to_list():

    with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'a') as f:
        f.write(f"{index+1}: " + ' '.join(map(str, krypterat_medelande)) + "\n")
    
    '''with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'r') as fp:
        for count, line in enumerate(fp):
            index = count'''

while True:
    medelande = input('Skriv ett medelande:     ')
    hemligt_medelande.clear()
    dekrypterat_medelande.clear()
    krypterat_medelande.clear()
    
    for letter in medelande:
        hemligt_medelande.append(letter)
        
    crypt()
    de_crypt()
    print(*krypterat_medelande)
    add_crypt_to_list()
    get_crypt_by_index()
    index += 1

    print(krypterat_medelande)
    print(dekrypterat_medelande)
    print()