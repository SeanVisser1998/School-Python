'''
Created on 13 Sep 2018

@author: seanv
'''
'''
    Opdracht 9
    
    EULEEEEERRRR <3
    https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem
    
    DEZE MAN IS EEN FUCKING LEGEND <3
    
    Een getal is perfect als 2**p -1 een priem is <3
'''
import math
import time

primes = []
def is_prime(n):
    
    appendPrime = primes.append
    if n == 1:
        return False
    
    if n == 2:
        appendPrime(n)
        return True
    
    if n > 2 and n%2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    appendPrime(n)
    return True
   
    
def findPerfectNumber(limit):
    for p in primes:
        pp = 2**p
        perfect = (pp - 1) * (pp // 2)
        if perfect > limit:
            break
        elif is_prime(pp - 1):
            print(perfect, "is a perfect number") 

T0 = time.time()
limit = 100000
for n in range(1, limit):
    is_prime(n)
findPerfectNumber(limit)
T1 = time.time()
print("Benodigde tijd:", T1-T0)
