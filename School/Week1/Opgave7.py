'''
Created on 12 Sep 2018

@author: seanv
'''
def isPalindroom(string):
    if str(string.lower()) == str(string.lower())[::-1]:
        return True
    else:
        return False
    
    
print(isPalindroom(""))