'''
Created on 15 Feb 2019

@author: seanv

IDK... Rare opdracht, maar hulpmiddel om die berekeningen te doen enzo ;)
'''

from Week21 import opdracht2
import math

'''
    RSA Decryption key GEN
    
    Ax + By = GCD(A,B)
    A = n(B) + R
    bla bla bla
'''

def euclids(a, b):
    b1 = b
    D = 0
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    if b == 1:
        D = (x0%b1)
    return D
    
'''
    Hopelijk is het te begrijpen :(
'''
    
print(modInv(21,160))

def a(e, p, q):
    n = p *q
    return (math.gcd(e, opdracht2.phi(n)))


def d(p, q, e, M):
    n = p*q
    return (M**e)%n # C= M^e Mod N

def e(C, key, N):
    return (C**key) % N
    

#Maken van de decryptie key, alleen is fout... 
# BEIDE waardes zijn PUBLIEK beschikbaar... En t klopt niet :(
print(makeD(77, 1889*1997))

#Opdracht 4A
print(a(77, 1997, 1889))

#Opdracht 4D
print(d(1889, 1997, 77, 290998))

#Opdracht e
print(e(623727, 3768448, 1889*1997))
