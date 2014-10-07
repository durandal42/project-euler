'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import common

def sum_proper_divisors(n):
  return sum(common.divisors(n)) - n

common.assertEquals(284, sum_proper_divisors(220))
common.assertEquals(220, sum_proper_divisors(284))

def amicable(n):
  other = sum_proper_divisors(n)
  return n != other and sum_proper_divisors(other) == n

common.assertEquals(True, amicable(220))
common.assertEquals(True, amicable(284))
common.assertEquals(False, amicable(12))
common.assertEquals(False, amicable(6))  # perfect numbers are not amicable with themselves

total = sum(i for i in range(1,10001) if amicable(i))
common.submit(total, expected=31626)
