'''
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import common
import math

def euler024(digits, index):
  index -= 1  # problem spec uses 1-based counting
  
  # base case: nothing to permute
  if not digits: return ""

  # for each option for the leading digit, we'll see this many tails:
  num_tails = math.factorial(len(digits)-1)

  # skip straight to the correct leading digit:
  i = index / num_tails
  head = digits[i]

  remaining_digits = digits[:i] + digits[i+1:]

  # recursively compute the correct tail:
  tail_index = index % num_tails
  tail = euler024(remaining_digits,
                  tail_index + 1)  # problem spec uses 1-based counting

  return head + tail

common.assertEquals("210", euler024("012", 6))

common.submit(euler024("0123456789", 10**6), expected="2783915460")
