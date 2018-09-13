'''
Created on 12 Sep 2018

@author: seanv
'''
def isPalindroom(string):
    if str(string) == str(string)[::-1]:
        return True
    else:
        return False
    
    
print(isPalindroom("Hond"))