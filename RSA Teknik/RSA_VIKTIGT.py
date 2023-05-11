hemligt_medelande = []
krypterat_medelande = []

medelande = 'bla bla'

print(medelande)
print(medelande.splitlines())
print([medelande])

p = 1009
q = 2003
n = p*q

phi=(p-1)*(q-1)

e = 1009037
d = 730661

m = int( input('Mata in ett tal med fyra siffror: ') )

#crypt
enc=pow(m,e,n)

#De crypt
dec=pow(enc,d,n)

print('Ditt meddelande är',m,sep=' ')
print('Kryptotexten är',enc,sep=' ')
print('Dekrypterad är',dec,sep=' ')