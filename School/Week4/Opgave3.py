'''
Created on 8 Oct 2018

@author: seanv

Benodigd: matplotlib
'''

import pandas
import matplotlib.pyplot as plt
from collections import Counter

astronaut_text = open(r"C:\Users\seanv\Desktop\astronaut.txt", 'r')

words = astronaut_text.read().split()


data = Counter(words).sort_index()
plt.bar(10, list(data.values()), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.show()

print(data)
