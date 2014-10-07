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
  data = [[None] * size for i in range(size)]

  # start in the middle...
  i = size/2
  j = size/2

  # moving right...
  di = 0
  dj = 1

  for count in itertools.count(1):
    data[i][j] = count
    if count == size*size:
      break
    i,j = i+di, j+dj

    # see if we can turn
    ndi, ndj = dj, -di  # speculatively turn clockwise
    if data[i+ndi][j+ndj] is None:  # if there's nothing in our new direction...
      di, dj = ndi, ndj  # ... commit to it.

  return (sum(data[i][i] + data[i][size-i-1] for i in range(size))
           - 1)  # don't double-count center

common.assertEquals(101, euler028(5))

common.submit(euler028(1001), expected=669171001)
