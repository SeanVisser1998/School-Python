import time
from turtle import *
from random import *

def flakeside(sidelength, level):
  ''' Draws the flakeside function in slowflake

  sidelength: Pixels of the flakeside line

  level: number of recursive levels

  '''

  print("Level bij start:",level)
  if level == 0:

    forward(sidelength)
    return 

  else:
    flakeside(sidelength/3, level -1)
    right(60)
    flakeside(sidelength/3, level -1)
    left(120)
    flakeside(sidelength/3,level-1)
    right(60)
    flakeside(sidelength/3, level -1)

reset()
flakeside(100,0)
reset()
flakeside(100,1)
reset()
flakeside(100,2)
