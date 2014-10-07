'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import common
import itertools

def sum_primes_below(n):
  return sum(itertools.takewhile(lambda x: x < n,
                                 common.primes()))

common.assertEquals(17, sum_primes_below(10))

common.submit(sum_primes_below(2000000), expected=142913828922)
