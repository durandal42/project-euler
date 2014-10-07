'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import common

def euler001(limit):
  return sum(i for i in range(limit) if not i % 3 or not i % 5)

common.assertEquals(23, euler001(10))

common.submit(euler001(1000), expected=233168)
