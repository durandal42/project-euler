'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import common

def find_triple(desired_sum):
  for a in range(1, desired_sum):
    for b in range(a + 1, desired_sum - a):
      c = desired_sum - a - b
      if a*a + b*b == c*c:
        return a*b*c

common.assertEquals(3*4*5, find_triple(12))

common.submit(find_triple(1000), expected=31875000)
