'''
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
'''

import common
import itertools

def goldbach(n):
  assert n%2 == 1
  for i in itertools.count():
    if common.prime(n - 2*i*i):
      return True
    if 2*i*i > n:
      return False

common.assertEquals(True, goldbach(9))
common.assertEquals(True, goldbach(15))
common.assertEquals(True, goldbach(21))
common.assertEquals(True, goldbach(25))
common.assertEquals(True, goldbach(27))
common.assertEquals(True, goldbach(33))

common.assertEquals(True, goldbach(7))  # it works for primes too! ^_^
# TODO(goldbach): think of a False test case

def euler046():
  for n in itertools.count(3, 2):
    if not goldbach(n):
      return n

common.submit(euler046(), expected=5777)
