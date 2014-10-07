'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
'''

import collections
import common
import itertools

def distinct_prime_factors(n):
  return collections.Counter(common.factor(n)).keys()

common.assertEquals([2, 7], sorted(distinct_prime_factors(14)))
common.assertEquals([3, 5], sorted(distinct_prime_factors(15)))
common.assertEquals([2, 7, 23], sorted(distinct_prime_factors(644)))
common.assertEquals([3, 5, 43], sorted(distinct_prime_factors(645)))
common.assertEquals([2, 17, 19], sorted(distinct_prime_factors(646)))

def euler047(n):
  result = []
  for i in itertools.count(2):
    if len(distinct_prime_factors(i)) == n:
      result.append(i)
      if len(result) == n:
        return result[0]
    else:
      result = []

common.assertEquals(14, euler047(2))
common.assertEquals(644, euler047(3))

common.submit(euler047(4), expected=134043)  # final submission, with post-hoc test
