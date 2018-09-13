'''
Created on 12 Sep 2018

@author: seanv
'''
from sys import stdin
NUMBER_OF_DAYS = 10
NUMBER_OF_HOURS = 24
data = []
for i in range(NUMBER_OF_DAYS):
    data.append([])
for j in range(NUMBER_OF_HOURS):
    data[i].append([])
# read input using input redirection from a file
for line in stdin:
    if line[0] == '#':
        continue
    L = line.strip().split()
 # ... hier jouw code ...
print("Gemiddelde temperaturen: ")
# find the average daily temperature
for i in range(NUMBER_OF_DAYS):
    print("hi")
