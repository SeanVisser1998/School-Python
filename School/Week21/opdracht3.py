'''
Created on 15 Feb 2019

@author: seanv

Berekend (a^Phi(N))%n
'''

from Week21 import opdracht2

def func(a, n):
    return ((a ** opdracht2.phi(n)) % n)

print(func(6,15))
