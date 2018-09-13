'''
Created on 13 Sep 2018

@author: seanv
'''
'''
    Opgave 3.A
'''
A = {'c':1, 'b':2, 'a':3, 'e':1, 'd':3}
def sortDic(dictionary):
    gesorteerd = sorted(dictionary.items(), key=lambda x: x[0])
    return gesorteerd

#print(sortDic(A))

'''
    Opgave 3.B
'''
B = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3, 'f': 5} 

def uniqueValueDic(dictionary):
    new_dict = {}
    countMap = {}
    
    for v in dictionary.values():
        countMap[v] = countMap.get(0,v) + 1
    
    uni = [k for k, v in dictionary.items() if countMap[v] == 1]
    
    for items in uni:
        if items in dictionary:
            new_dict.update({items:dictionary[items]})
            
    return new_dict
print(uniqueValueDic(B))
    
    
def uniquevalueDicV2(dictionary):
    L = list(dictionary.values())
    L = [x for x in L if L.count(x) is 1]
    return L
'''
    Opgave 3.C
'''
C = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]

def uniqueValueList(List):
    result = []
    for i in range(len(List)):
        result.append(list(List[i].items())[0][1])
    result = set(result)
    return sorted(result)
print(uniqueValueList(C))