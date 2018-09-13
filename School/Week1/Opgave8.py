'''
Created on 12 Sep 2018

@author: seanv
'''
import math

def gevoelsTemperatuur(T, B):
    G = 13 + 0.62*T - math.pow(14*B, 0.24) + 0.47*T*math.pow(B, 0.24)
    return G