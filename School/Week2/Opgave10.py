'''
Created on 13 Sep 2018

@author: seanv
'''
import matplotlib.pyplot as plt
from collections import Counter
from string import ascii_lowercase

astronaut_text = open(r"C:\Users\seanv\Desktop\astronaut.txt", 'r')


def countLetters(text):
    with text as f:
        return Counter(letter for line in f
                for letter in line.lower()
                if letter in ascii_lowercase)
        
Data = countLetters(astronaut_text)
plt.bar(range(len(Data)), list(Data.values()), align='center')
plt.xticks(range(len(Data)), list(Data.keys()))
plt.title("Lettergebruik in tekst")
plt.show()

