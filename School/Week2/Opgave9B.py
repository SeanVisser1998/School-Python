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
n_array = [2,3,5,7,13,17,19,31,61,89,107]

#Arrays waarin de priem getallen gegooid worden <3
perfect_numbers = []

def perfectNoLimit():
    s = 1
    appendPerfect = perfect_numbers.append #Haalt de append functie buiten de for loop, om code te versnellen
    for n in range(len(n_array) -1): #Voor de n waardes in de lengte van n_array-1

        i = int(n_array[n]) #Zet i gelijk aan de waarde van n_array op index n
        perfect = math.pow(2, i-1) * (math.pow(2, i) -1) #Vult de formule voor perfecte getallen in
        print("{0}e Perfect getal: {1} ".format(s, perfect)) #Print de perfecte getallen
        appendPerfect(perfect) #Append de perfecte getallen naar perfect_numbers. Hier staat eigenlijkL perfect_numbers.append(perfect)
        s += 1 #Increment de count van het perfecte getal met 1


#Precies hetzelgde als perfectNoLimit() alleen dan print deze NIKS
def perfectNoLimitNoPrint():
    s = 1
    appendPerfect = perfect_numbers.append
    for n in range(len(n_array) -1):

        i = int(n_array[n])
        perfect = math.pow(2, i-1) * (math.pow(2, i) -1)
        appendPerfect(perfect)
        s += 1

#Precies hetzelfde als de anderen, alleen deze print alleen de  perfecte getallen als ze lager zijn dan het meegegeven limiet
def perfectLimit(limit):
    s = 1
    for n in range(len(n_array)):
        i = int(n_array[n])
        perfect = math.pow(2, i-1) * (math.pow(2, i) -1)
        if perfect <=  limit: #Als het perfecte getal lager is dan het limiet, dan....
            print("{0}e Perfect getal: {1}".format(s,perfect))
            s += 1

#kijkt of het meegegeven getal een perfect getal is
def isPerfectNumber(number):
    perfectNoLimitNoPrint() #Runt perfectNoLimitNoPrint()
    if(number in perfect_numbers): #Als number voorkomt in perfect_numbers, is het een perfect getal
        print("{0} is WEL een perfect getal!".format(number))
        return True
    else:
        #print("{0} is GEEN perfect getal!".format(number))
        return False

''' 
    TRAAAAAAGG
'''
#T0 = time.time()
#for n in range(1,10000):
#    isPerfectNumber(n) #TRAAAAAAAAAGGGG
#T1 = time.time()
#print("Benodigde tijd: {0} seconden ".format(T1 - T0))

'''
    SNEEEEEELLL <3
''' 
T2 = time.time()
perfectLimit(10000)
T3 = time.time()
print("Benodigde tijd: {0} seconden ".format(T3 - T2))
