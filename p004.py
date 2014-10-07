'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import common

def euler004(digits):
  return max(i*j
             for i in range(10**(digits-1), 10**digits)
             for j in range(i, 10**digits)
             if common.palindrome(i*j))

common.assertEquals(9009, euler004(2))

common.submit(euler004(3), expected=906609)

