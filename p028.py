'''
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
'''

import common
import itertools

def euler028(size):
  # 2D array size*size, initially all None
  data = [[None] * size for i in range(size)]

  # start in the middle...
  i, j = size/2, size/2
  # moving right...
  di, dj = 0, 1

  for count in range(1, size*size):
    data[i][j] = count
    i += di
    j += dj

    # see if we can turn
    ndi, ndj = dj, -di  # speculatively turn clockwise
    if data[i + ndi][j + ndj] is None:  # if there's nothing in our new direction...
      di, dj = ndi, ndj  # ... commit to it.

  data[i][j] = size*size

  return (sum(data[i][i] + data[i][-i - 1] for i in range(size))
           - 1)  # don't double-count center

# Diagonals grow as size**2, and we're summing them, so euler028 is O(size**3).
# Fit a cubic to the first four data points (we can always fit an exact cubic to 4 points)
#   and check it against the fifth.
import numpy
import fractions
def find_closed_form(f, data, test=[], hardcode=False):
  coefficients = numpy.polyfit(data, map(f, data), 3)
  rational_coefficients = [fractions.Fraction(c).limit_denominator() for c in coefficients]
  print rational_coefficients
  result = lambda size: sum(size ** p * c for p,c in enumerate(reversed(rational_coefficients)))
  for x in test:
    assert result(x) == f(x)
  return result

euler028 = find_closed_form(euler028, [1,3,5,7], [9])

common.assertEquals(101, euler028(5))

common.submit(euler028(1001), expected=669171001)

# Just showing off; given a closed form, these are essentially free to compute:
print euler028(1000001)
print euler028(1000000001)
print euler028(1000000000001)
print euler028(1000000000000001)
