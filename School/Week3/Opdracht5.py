'''
Created on 24 Sep 2018

@author: seanv
'''

'''

=) is gemaakt :3
  De Stack class maakt het mogelijk om objecten in een stapel te bewaren en biedt operaties om de stack te
  bewerken. De class Stack heeft de volgende attributen:
    field elements: list (private) list to store the elements in the stack
    =) method constructor creates an empty stack
    =) method is_empty() returns True if the stack is empty
    =) method peek() returns the element at the top of the stack without
    removing it from the stack
    =) method push(value: object) stores an element at the top of the stack
    =) method pop() removes the element at the top of the stack and returns it
    method getSize() returns the number of elements in the stack  
'''

#Class Stack aanmaken
class Stack():
    
    #Class Stack initialiseren
    def __init__(self):
        #Maakt een array :3
        self.__elements = []
    
    #Functie om te kijken of de array leeg is
        '''
        Returned: True | False
        Parameters: self 
        
        
        gebruik: Stack().isEmpty()
    '''
    def isEmpty(self):
        #Kijkt of de lengte van de array 0 is, want dan is die leeg =)
        if len(self.__elements) == 0:
            return True #Returned true, want len(self.__elements) ==0
        else:
            return False #Returned False, want len(self.__elements) !=0
    
    #Functie om een waarde in de array te pushen :3
    '''
        Returned: Niks
        Parameters: self & waarde
        
        waarde is de waarde die naar de array gepushed moet worden
        
        gebruik: Stack().push(self, waarde)
    '''
    def push(self, waarde):
        #Append de waarde meegegeven als parameter naar de stack
        self.__elements.append(waarde)
        
        
    #Functie om de eerste waarde in de stack te verwijderen (pop)
    '''
        Returned: Eerste element in stack
        Parameters: self 
    
        
        gebruik: Stack().pop()
    '''
    def pop(self):
        pop = self.__elements[0] #Maakt gebruik van tussen/tmp waarde om het eerste element in de stack te returnen
        self.__elements.pop(0)
        return pop
        
    #Functi eom de eerste waarde in de stack te bekijken, zonder deze te verwijderen :3
        '''
        Returned: Eerste waarde uit stack
        Parameters: self
        
        gebruik: print(Stack().peek())
    '''
    def peek(self):
        return self.__elements[0]
    
    
stack = Stack() #Maakt niet Stack object
stack.push(10) #pushed 10 in de stack
stack.push(20) #Pushed 20 in de stack
print(stack.peek()) #10
print(stack.pop()) #Popped de eerste waarde (index 0) in de stack
print(stack.peek()) #20
