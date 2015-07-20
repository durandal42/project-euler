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
  i, j = (size-1)/2, (size-1)/2
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
           - size % 2)  # if size is odd, the center square (1) is in both diagonals.

# Diagonals grow as size**2, and we're summing them, so euler028 is O(size**3).
# Fit a cubic to the first four data points (we can always fit an exact cubic to 4 points)
#   and check it against the fifth.
import numpy
import fractions
def find_closed_form(f, data, test=[]):
  coefficients = numpy.polyfit(data, map(f, data), len(data)-1)
  rational_coefficients = [fractions.Fraction(c).limit_denominator() for c in coefficients]
  print rational_coefficients
  result = lambda size: sum(size ** p * c for p,c in enumerate(reversed(rational_coefficients)))
  for x in test:
    assert result(x) == f(x)
  return result

# The antidiagonal is in a different location depending on the parity of size, so don't expect
# the same formula to hold for both odd and even sizes.
euler028_odd = find_closed_form(euler028, [1,3,5,7], [9])
euler028_even = find_closed_form(euler028, [2,4,6,8], [10])
euler028 = lambda size: [euler028_even, euler028_odd][size%2](size)

common.assertEquals(101, euler028(5))

common.submit(euler028(1001), expected=669171001)

# Just showing off; given a closed form, these are essentially free to compute:
print euler028(1000000)
print euler028(1000001)
print euler028(1000000000)
print euler028(1000000001)
print euler028(1000000000000)
print euler028(1000000000001)
print euler028(1000000000000000)
print euler028(1000000000000001)
