'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import common
import math

def curious(n):
  return sum(math.factorial(int(d)) for d in str(n)) == n

common.assertEquals(True, curious(145))
common.assertEquals(False, curious(144))

all_curious = [i for i in range(10, 50000) if curious(i)]
print all_curious

common.submit(sum(all_curious), expected=40730)
