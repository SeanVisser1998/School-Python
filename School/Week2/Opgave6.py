'''
Created on 13 Sep 2018

@author: seanv
'''

'''
    Opdracht 6.A
'''
L = [1,2,3,3,3,3,4,5] 

def unique_list(List):
    unique = list(set(List)) #Unieke list ONGEORDENED
    return unique
print(unique_list(L))

'''
    Opdracht 6.B
'''
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_elements(List):
    even = [i for i in List if i%2==0]
    return even
print(even_elements(L2))

'''
    Opdracht 6.C
'''

def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase.lower():
            return False
    return True
print(is_pangram("Filmquiz bracht knappe ex-yogi van de wijs"))

'''
    Opdracht 6.D
'''
dic = {'ed': 5, 'carl':3, 'alan':1, 'bob':2, 'dan':4}

def sortDic(dictionary):
    gesorteerd = sorted(dictionary.items(), key=lambda x: x[0])
    return gesorteerd
print(sortDic(dic))