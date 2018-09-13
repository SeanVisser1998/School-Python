'''
Created on 13 Sep 2018

@author: Hugh Bothwell @StackOverflow.com <33333 (VEEEEL SNELLER DAN DAT IK T OOIT HAD KUNNEN BEDENKEN :3)
'''

import time
def primes(known_primes=[7, 11, 13, 17, 19, 23, 29]):

  
    yield from (2, 3, 5)
    yield from known_primes
    base = 30 * (known_primes[-1] // 30 + 1)
    new_primes = []
    while True:
    
        for offs in (1, 7, 11, 13, 17, 19, 23, 29):
            k = base + offs
            for p in known_primes:
                if not k % p:
                   
                    break
                elif p*p > k:
                   
                    new_primes.append(k)
                    break
        if new_primes:
            yield from new_primes
            known_primes.extend(new_primes)
            new_primes = []
        base += 30

def is_prime(n):
    for p in primes():
        if not n % p:
            
            return False
        elif p * p > n:
        
            return True
        
def findPerfectNumber(limit):
    for p in primes():
        pp = 2**p
        perfect = (pp - 1) * (pp // 2)
        if perfect > limit:
            break
        elif is_prime(pp - 1):
            print(perfect, "is a perfect number")
            
T0 = time.time()
findPerfectNumber(250000000000)
T1 = time.time()
print("Benodigde tijd: ", T1-T0)