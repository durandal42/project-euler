'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

import common

def euler005(limit):
    return reduce(common.lcm, range(1, limit + 1))

common.assertEquals(2520, euler005(10))

common.submit(euler005(20), expected=232792560)
