'''
Created on 15 Feb 2019

@author: seanv

IDK... Rare opdracht, maar hulpmiddel om die berekeningen te doen enzo ;)
'''

from Week21 import opdracht2
import math

def makeD(e, n):
    # D * e + phi(n) = 1
    pass

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
