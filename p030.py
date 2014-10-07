'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import common
import itertools

def solution_length(power):
  # find out how many digits could be in the solution:
  for digits in itertools.count(1):
    if len(str(9**power * digits)) < digits:
      # if all 9's can't reach the digit count, we've gone too far
      return digits-1

assertEquals(True, 4 <= solution_length(4))  # example numbers have 4 digits

def euler030(power):
  return sum(i for i in xrange(2, 9**power * solution_length(power))
             if sum([int(x)**power for x in str(i)]) == i)
  return total

common.assertEquals(19316, euler030(4))
common.submit(euler030(5), expected=443839)
