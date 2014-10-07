'''It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
'''

import common
import itertools

def digits(x):
  return set(int(d) for d in str(x))

common.assertEquals(digits(125874), digits(251748))

def same_digits_as_multiples(x, multiples):
  d = digits(x)

  # duplicate digits are implicitly forbidden
  if len(d) != len(str(x)): return False

  for i in multiples:
    if d != digits(i*x):
      return False
  return True

common.assertEquals(True, same_digits_as_multiples(125874, [2]))
common.assertEquals(False, same_digits_as_multiples(123456, [2]))

def euler052():
  multiples = range(2,7)
  for i in itertools.count(10**5):  # solution must have at least 6 digits
    if same_digits_as_multiples(i, multiples):
      return i

common.submit(euler052(), expected=142857)