'''
Starting in the top left corner of a 2*2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20*20 grid?
'''

import common
import math

def euler015(n):
    return math.factorial(2*n) / math.factorial(n)**2

common.assertEquals(6, euler015(2))

common.submit(euler015(20), expected=137846528820)
