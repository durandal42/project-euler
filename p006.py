'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''

import common

def euler006(limit):
  r = range(1, limit + 1)
  return sum(r)**2 - sum(i**2 for i in r)

common.assertEquals(2640, euler006(10))

common.submit(euler006(100), expected=25164150)
