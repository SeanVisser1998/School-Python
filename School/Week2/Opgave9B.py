'''
Created on 16 Sep 2018

@author: seanv
'''

import math
import time

'''
    Wat is een perfect getal?? 
    
    Euler heeft beschreven dat een perfect getal voldoet aan 2^n (2^(n+1) -1)
    
    waarbij (2^(n+1) -1) een priem getal is.
    
    (2^(n+1) -1) is ook de algemene formule voor mersenneprimes :3 
    
    Hiermee kunnen wij dus ontzettend snel enorm grote perfecte getallen maken :3

    In dit programma zullen wij de eerste 10 mersenne primes gebruiken :3

'''

#N-waarden voor mersenne primes <3
n_array = [2,3,5,7,13,17,19,31,61,89]

def perfectNoLimit():
    s = 1
    for n in range(len(n_array) -1):

        i = int(n_array[n])
        perfect = math.pow(2, i-1) * (math.pow(2, i) -1)
        print("{0}e Perfect getal: {1} ".format(s, perfect))
        s += 1

def perfectLimit(limit):
    s = 1
    for n in range(len(n_array)):
        i = int(n_array[n])
        perfect = math.pow(2, i-1) * (math.pow(2, i) -1)
        if perfect <=  limit:
            print("{0}e Perfect getal: {1}".format(s,perfect))
            s += 1

T0 = time.time()
perfectNoLimit()
T1 = time.time()
print("Benodigde tijd: {0} seconden ".format(T1 - T0))