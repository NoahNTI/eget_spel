import random
from math import gcd

def generate_rsa_keys():
    while True:
        p = random.randint(1000, 10000)
        if is_prime(p):
            break
    
    while True:
        q = random.randint(1000, 10000)
        if is_prime(q) and q != p:
            break
            
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
    
    d = modinv(e, phi)
    
    return p, q, n, phi, e, d

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)
    
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        raise Exception('No modular inverse')
    else:
        return x % m

def tolk_pq_rsa_hund_krypterningsmakapärishnycklar_för_lösning_apa_med_bannnanna_hej_jag_hetger_mångs(index_to_get):
    index_to_get = int(input('What index number are you looking for:    '))

    with open('egna_spel/RSA_Teknik/krypterade_medelande.txt', 'r') as f:
        for line in f:
            if line.startswith(f"{index_to_get}:"):
                
                crypt_str = line.split(":")[1].strip()
                crypt_numbers = [int(x) for x in crypt_str.split()]
                
                print(f"The incrypted version is {crypt_numbers} \nThe cryptated version is:")
