'''
Created on 15 Feb 2019

@author: seanv

IDK... Rare opdracht, maar hulpmiddel om die berekeningen te doen enzo ;)
'''

from Week21 import opdracht2
import math

def makeD(e, p,q):
    # E * D == 1 mod phi((q-1)(p-1))
    # D = (1 mod phi((q-1)(p-1))/e  (Modulo werkt niet zo vgm tho...)
    
    # D = 1 mod (q-1)(p-1) / E
    
    # return ((1 % ((q-1)(p-1)) / e) (?)
    D = 0
    while e * D not (1 % opdracht2.phi((q-1)*(p-1))):
         D +=1
    return D

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
