'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import common
import itertools

@common.memoized
def right_truncatable(n):
  if n > 10 and not right_truncatable(n/10): return False
  if not common.prime(n): return False
  return True

@common.memoized
def left_truncatable(n):
  if n > 10 and not left_truncatable(int(str(n)[1:])): return False
  if not common.prime(n): return False
  return True

def truncatable(n):
  return n >= 10 and left_truncatable(n) and right_truncatable(n)

common.assertEquals(True, truncatable(3797))
common.assertEquals(False, truncatable(3))
common.assertEquals(False, truncatable(41))

total = sum(itertools.islice((i for i in itertools.count() if truncatable(i)), 11))

common.submit(total, expected=748317)
