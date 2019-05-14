'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import common
import itertools


def euler050(n):
  best = (0, None)
  for i in itertools.count():
    if common.nth_prime(i) > n:
      break
    running_sum = 0
    for j in itertools.count(i):
      running_sum += common.nth_prime(j)
      if running_sum > n:
        break
      if common.prime(running_sum):
        best = max(best, (j - i, running_sum))
  return best[1]

common.assertEquals(41, euler050(100))
common.assertEquals(953, euler050(1000))

common.submit(euler050(10**6), expected=997651)
