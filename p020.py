'''
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import common
import math

def euler020(n):
  return sum(int(d) for d in str(math.factorial(n)))

common.assertEquals(27, euler020(10))

common.submit(euler020(100), expected=648)
