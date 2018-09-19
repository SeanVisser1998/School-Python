from math import pi

class Circle():
    
    def __init__(self, straal):
        self.straal = straal
    
    def area(self):
        return pi*(self.straal**2)
    
    def perimeter(self):
        return 2*self.straal*2
    
NewCircle = Circle(8)
print("Diameter van de cirkel: {0}".format(NewCircle.area()))