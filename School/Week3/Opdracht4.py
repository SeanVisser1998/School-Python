'''
Created on 19 Sep 2018

@author: Sean
'''

'''
    FUCK DIT IK BEN HIER ZO KLAAR MEE, CLASSES IN PYTHON IS BULLSHIT =(
'''

#Class Roman
class roman():
    
    #Dictionary de we gaan gebruiken om romeinse 'cijfers' aan onze cijfers te koppelen
    rom_value= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    #Initialisatie van de klasse
    def __init__(self, csl, s):
        self.csl = csl
        self.s = s
    
    def roman_to_int(self, csl, s):
        self.csl = csl
        self.s = s
        print(s)
        print(csl)
        
Integer = roman('X','X')