'''
Created on 24 Sep 2018

@author: seanv
'''
import time #Import de module time uit de standaart Python library

class Stopwatch():
    
    #Initaliseert de classe Stopwatch
    def __init__(self):
        self.__startTime = 0 #Zet begin waarde van __startTime op 0
        self.__stopTime = 0 #Zet begin waardew van __stopTime op 0
        self.__diffTime = 0 #Zet begin waarde van __digTime op 0

    #Functie die de stopwatch start
    '''
        Returned: self.__startTime
        Geeft de starttijd terug
        
        Functie die de huidige tijd toekend aan self.startTime
    '''       
    def startWatch(self):
        self.__startTime = time.time() #__startTime wordt gelijk gezet aan de huidige tijd
        return self.__startTime #self.__startTime wordt gereturned
        #START DE STOPWATCH
        
    #Functie die de stopwatch stopt
    '''
        Returned: self.__diffTime
        Geeft self.__stopTime - self.__startTime terug
        
        Functie die het verschil tussen self.__startTime en self.__stopTime toekend aan self.__diffTime
    '''
    def stopWatch(self):
        self.__stopTime = time.time() #__stopTime wordt gelijk gezet aan de huidige tijd
        self.__diffTime = self.__stopTime - self.__startTime #Verschil tussen __stopTime & __startTime (AKA: Hoelang het heeft geduurd)
        return self.__diffTime #Returned het verschil tussen __stopTime & __startTime
        
        
    #Functie die de stopwatch reset (alle waardes weer naar 0)
    '''
        Returned: null
        Zet self.__stopTime, self.__startTime & self.__diffTime naar 0
        
        Functie die de stopwatch reset
    '''
    def resetWatch(self):
        self.__diffTime = 0 #__diffTime wordt naar 0 gezet(reset)
        self.__startTime = 0 #__startTime wordt naar 0 gezet(reset)
        self.__stopTime = 0 #__stopTime wordt naar 0 gezet(reset)
        
        

stopwatch = Stopwatch()
print(stopwatch.startWatch())
print(stopwatch.stopWatch())
