'''
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

import collections
import common
import math

# Instead of trying every possible p and counting the number of (a,b,c) solutions,
# try every (a,b) that fit within the upper bound, compute what c would have to be,
# and credit the appropriate total.
# Further optimizations:
# 1) assume a < b, without loss of generality
# 2) a <= total/(2+sqrt(2)); given #1, a's proportion of the perimeter is maximized
#    in an equilateral right triangle, in which the sides have ratio 1:1:sqrt(2)
# 3) b < (p - a) / 2; with a fixed, b can't be more than half the remaining perimeter
def all_totals(limit):
  for a in range(1, int(limit / (2+math.sqrt(2)))):
    for b in range(a, (limit-a)/2):
      c = math.sqrt(a*a + b*b)
      total = a+b+c
      if c == int(c) and total <= limit:
        yield int(total)

result = max((v,k) for k,v in collections.Counter(all_totals(1000)).iteritems())[1]

common.submit(result, expected=840)
