'''
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
'''

import common
import itertools

def sequence():
  for i in itertools.count(1):
    for d in str(i):
      yield int(d)

def euler040(indices):
  return common.product(
    d
    for i,d in enumerate(itertools.islice(sequence(), max(indices)))
    if i+1 in indices)

common.assertEquals(1, euler040([12]))

result = euler040([1, 10, 100, 1000, 10000, 100000, 1000000])

common.submit(result, expected=210)
