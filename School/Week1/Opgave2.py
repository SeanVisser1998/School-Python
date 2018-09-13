'''
Created on 12 Sep 2018

@author: seanv
'''

import random
L = [30, 1,2,1,0,"hello","Goodbye"]

print(L.index(1)) #1
print(L.count(1)) #2
print(len(L)) #7 
#max(L) #ERROR '>' NOT SUPPORTED
L.append(40) #Voegt 40 aan het einde van de list toe
L.insert(1, 43) #Voegt 43 op index 1 toe
L.extend([1, 43]) #Zelfde als append in dit geval
L.remove("hello") #Verwijders "Hallo"
L.pop() #returnt index waarde
"Goodbye" in L #JA
L.pop(3) #Returned indexwaarde 3
L.sort() #ERROR
random.shuffle(L) #TypeERROR
