'''
Created on 13 Sep 2018

@author: seanv
'''
'''
    Opdracht 5.A
'''
array_cap = ["H", "s", "r"]

def capitalize_all(t):
    result = [s.capitalize() for s in t]
    return result

print(capitalize_all(array_cap))

'''
    Opdracht 5.B
'''
def only_upper(t):
    result = [s for s in t if s.isupper()]
    return result
print(only_upper(array_cap))