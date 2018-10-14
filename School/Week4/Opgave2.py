'''
Created on 8 Oct 2018

@author: seanv

Benodigdheden: Pandas 

Installatie: CMD > Pip install pandas
'''

import pandas

df = pandas.read_json(r'C:\Users\seanv\Desktop\books.json')

print(df.head())
def getGemiddeldePrijs(dataframe):
    return dataframe['Price'].mean().round(2)


def sortLastName(dataframe):
    dataframe['achternaam'] = dataframe['author'].str.split().str[-1]
    return dataframe.sort_values(by=['author'])

print(sortLastName(df))