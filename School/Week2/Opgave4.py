'''
Created on 13 Sep 2018

@author: seanv
'''

'''
    Opdracht 4.A
'''
s1 = {1,4,5,6}
s2 ={1,3,6,7}

def findCommonDict(D1, D2):
    intersect = D1.intersection(D2)
    return intersect

'''
    Opdracht 4.B
'''

def findDifferenceDict(D1, D2):
    symDif = D1.symmetric_difference(D2)
    return symDif
print ( findDifferenceDict(s1, s2))


'''
    Opdracht 4.C
'''
L = [1, 7, 4, 8, 9, 9, 4, 1, 4, 11, 14, 21, 15, 5, 2, 5]
def isInList(value, List):
    return (value in List)
print(isInList(11, L))
    