'''
Created on 19 Sep 2018

@author: Sean
'''
class roman():
    
    rom_value= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    def __init__(self, cls, s):
        self.csl = cls
        self.s = s
    
    def roman_to_int(self):
        int_val = 0