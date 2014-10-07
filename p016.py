'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import common

def euler016(n):
  return sum(int(d) for d in str(2**n))

common.assertEquals(26, euler016(15))

common.submit(euler016(1000), expected=1366)
