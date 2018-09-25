'''
Created on 25 Sep 2018

@author: Sean
'''

'''
    Zeeslag spel ofzo
    
    PS de opdracht in de weekopdracht slaat nergens op, dus ik heb er mijn eigen code voor gemaakt, maar het principe is hetzelfde =)
'''

class BattleShipGame():
    
    #Classe initalisatie
    def __init__(self, rondes):
        self.bootY = [] #Array om de Y-as locatie(s) van een boot op te slaan
        self.bootX = [] #Array om de X-as locatie(s) van een boot op te slaan
        self.guesses = [] #Array om de (eerder) gegokte boot Y & X locatie(s) in op te slaan
        self.turns = rondes #Hoeveelheid rondes in het spel(na x rondes is het spel afgelopen)
        
    
    #Functie die een boot toevoegd aan het spel
    def addBoot(self, x, y):
        self.bootX.append(x) #Slaat de X-as locatie van een boot op
        self.bootY.append(y) #Slaat de Y-as locatie van een boot op
        
    #Functie die de X-as & Y-as locaties van een boot print :3
    def getBoot(self):
        for i in range(len(self.bootY)):
            print("Boot nummer {0} is op locatie {1},{2}(X,Y)".format(i+1, self.bootX[i], self.bootY[i]))

    def guessBoot(self, x, y):
        if self.turns == 0: #Als het aantal rondes gelijk is aan 0, dan...
            print("Het spel is afgelopen =(") #Print ...
            return False
        if ((x in self.bootX) and (self.bootY[self.bootX.index(x)] == y)): #Als x in de array BootX zit EN de waarde van bootY is gelijk aan y op de index van x in bootX 
            print("Gefeliciteerd! Je hebt de boot geraakt!") #Print
            self.turns -= 1 #Verlaagt het aantal rondes met 1
            return True
        else:
            print("Jammer! Probeer het nog eens!") #Print...
            self.turns -= 1 #Verlaagt het aantal rondes met 1
            return False
        
    
game = BattleShipGame(4) #Init een zeeslagspel met 4 rondes
game.addBoot(2, 3)
game.getBoot()
game.guessBoot(1, 3) #JAMMER
game.guessBoot(2, 3) #GEFELICITEERD
game.guessBoot(3, 2) #JAMMER
game.guessBoot(3, 3) #JAMMER
game.guessBoot(1, 3) #Het spel is afgelopen =(
game.guessBoot(1, 3) #Het spel is afgelopen =(