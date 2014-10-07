'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import common

def double_palindrome(n):
  return common.palindrome(n) and common.palindrome(bin(n)[2:])

common.assertEquals(True, double_palindrome(585))
common.assertEquals(False, double_palindrome(575))

total = sum(i for i in xrange(1000000) if double_palindrome(i))

common.submit(total, expected=872187)
