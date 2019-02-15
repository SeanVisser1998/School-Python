'''
Created on 15 Feb 2019

@author: seanv
@version: 1.0.0
@requires: math

Description: Berekend Eulers totient =)
'''
import math
import time

def phi(n) :
     
    phi = n 

    p = 2
    while(p * p<= n) : 
        if (n % p == 0) : 
            while (n % p == 0) : 
                n = n // p 
            phi = phi * (1.0 - (1.0 / float(p))) 
        p = p + 1
    if (n > 1) : 
        phi = int(phi * (1.0 - (1.0 / float(n)))) 
   
    return (phi) 


#print(phi(3772333))
#t1 = time.time()
#print(phi(2628767))
#t2 = time.time()
#print(t2-t1)