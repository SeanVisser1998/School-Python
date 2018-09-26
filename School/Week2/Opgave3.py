'''
Created on 13 Sep 2018

@author: seanv
'''
'''
    Opgave 3.A
'''
A = {'c':1, 'b':2, 'a':3, 'e':1, 'd':3}
def sortDic(dictionary):
    gesorteerd = sorted(dictionary.items(), key=lambda x: x[0]) #Sorteerd wordt gesorteerd op de items, met behulp van een lambda functie. De lambda functie loopt erover op index 0
    return gesorteerd #Geeft gesorteerd terug

#print(sortDic(A))

'''
    Opgave 3.B
'''
B = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3, 'f': 5} 


#Parameter: dictionary
#Returned: alle unieke waardes in een array
def uniqueValueDic(dictionary):
    new_dict = {} #Maakt een nieuwe dictionary
    countMap = {} #Maakt een nieuwe dictianary voor de counts
    
    for v in dictionary.values(): #Voor elke value in de aan de functie megegeven parameter(dictionary) ...
        countMap[v] = countMap.get(0,v) + 1 #CountMap op index v(Values uit de parameter) is gelijk aan waardes +1
    
    uni = [k for k, v in dictionary.items() if countMap[v] == 1] #Unieke waardes
    
    for items in uni: #Vooe alle unieke items
        if items in dictionary: #Als het unieke item in de dicitonary zit, dan..
            new_dict.update({items:dictionary[items]}) #Stopt alle unieke items in de nieuwe dictionary <3
            
    return new_dict #Geeft de nieuwe dictionary terug
print(uniqueValueDic(B))
    

#Veel makkelijkere en kortere manier om alle unieke waarden in een dictionary terug te geven <3
#Parameter: Dictionary
#Returned: Lijst met alle unieke waardes
def uniquevalueDicV2(dictionary):  
    L = list(dictionary.values()) #L is een lijst van de values in de dictionary
    L = [x for x in L if L.count(x) is 1] #Wordt aan L toegevoegd als de count van de values in de dictionary maar een keer voorkomt
    return L #Geeft L terug
'''
    Opgave 3.C
'''
C = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

#Parameter: Lijst
#Returned: Gesorteerde lijst met unieke waarden uit de meegegven lijst
def uniqueValueList(List):
    result = [] #Maakt een lege array voor de resultaten
    for i in range(len(List)): #Zolang i past in de lengte van de aan de functie meegegeven lijst
        result.append(list(List[i].items())[0][1]) #Append de unieke waardes in de result array
    result = set(result) 
    return sorted(result) #Geeft de gesorteerde array terug
print(uniqueValueList(C))