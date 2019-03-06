'''
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
'''

import common

RAW_DATA = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''


def parse(raw_data):
  '''Parse text data into a tuple of tuples.

  Why tuples?
  1) Lists are mutable, which permitted an earlier version to destructively
     modify the data, which wasn't a problem for itself, but made it awkward to
     run multiple algorithms on the same data.
  2) Tuples are immutable, so they're hashable, so they can be used in memoization.
  '''
  return tuple(tuple(int(number) for number in line.split(" "))
               for line in raw_data.strip().split('\n'))

DATA = parse(RAW_DATA)


def euler018_dp(data):
  '''Dynamic programming.'''
  last = data[-1]
  for i in reversed(range(len(data) - 1)):
    last = tuple(p + max(last[j], last[j + 1]) for j, p in enumerate(data[i]))

  return last[0]


def euler018_brute(data, i=0, j=0):
  '''Easy, but far too slow on larger data.'''
  if i >= len(data):
    return 0
  return data[i][j] + max(euler018_brute(data, i + 1, j),
                          euler018_brute(data, i + 1, j + 1))


@common.memoized
def euler018_memoized(data, i=0, j=0):
  '''Just memoize the brute force solution.

  This is awkward, because the data itself has to be stored with each
  memoized call. :(
  '''
  if i >= len(data):
    return 0
  return data[i][j] + max(euler018_memoized(data, i + 1, j),
                          euler018_memoized(data, i + 1, j + 1))

# Which algorithm to use:
euler018 = euler018_dp

TEST_DATA = parse('''
3
7 4
2 4 6
8 5 9 3
''')
common.assertEquals(23, euler018(TEST_DATA))

common.submit(euler018(DATA), expected=1074)
