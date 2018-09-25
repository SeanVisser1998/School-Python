'''
Created on 19 Sep 2018

@author: Sean
'''

'''
    FUCK DIT IK BEN HIER ZO KLAAR MEE, CLASSES IN PYTHON IS BULLSHIT =(
'''

#Class Roman
class Roman():

    
    #Initialisatie van de klasse
    def __init__(self):
        self = self #initializatie van classe
    
    #Classe die aan de hand van de dictionary Roman omzet naar Cijfers
    ''' 
        Returned: Cijfer
        Geeft de waarde van de romeinse cijfers in onze cijfers terug
        
        Functie die aan de hand van de dictionary de romeinse cijfers vertaald naar onze cijfers
    '''
    def roman_to_int(self, roman):
        
           
        #Dictionary de we gaan gebruiken om romeinse 'cijfers' aan onze cijfers te koppelen
        rom_val= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        int_value = 0 #Zet de waarde van de integer (terug) op 0
        for i in range(len(roman)): #Blijft i ophogen tot het gelijk is aan de lengte van de roman
            if i > 0 and rom_val[roman[i]] > rom_val[roman[i-1]]: #Als i groter is dan 0 EN de rom_value[roman[i]] is GROTER DAN rom_val[roman[is]], DAN....
                int_value += rom_val[roman[i]] - 2 * rom_val[roman[i-1]]
            else:
                int_value += rom_val[roman[i]] #Int_value wordt met rom_val opgehoogd
        
        return int_value #Returned int_value
    
    
roman = Roman()
print(roman.roman_to_int('MMXVIII'))
                
    
    
        
