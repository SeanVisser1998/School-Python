'''
Created on 15 Feb 2019

@author: seanv
@version: 1.0.0
@requires: math

Description: Factoriseert een getal in zijn priem factoren :o
'''

import math

primes = []

def factorize(n):
    i = 2 #laagste priem getal
    append = primes.append
    while i * i <=n:
        if n % i: #Als n%2 gelijk is aan 1(Overgaan naar andere deler), dan...
            i += 1
        else:
            n //= i #Delen met weg gooien van het 'overblijfsel'
            append(i)
    if n > 1:
        append(n)
        
    return primes

print(factorize(73656))






