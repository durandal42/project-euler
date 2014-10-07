'''
The following iterative sequence is defined for the set of positive integers:
  n -> n/2 (if n is even)
  n -> 3n+1 (if n is odd)

Using the rule above and starting with 13, we generate the following sequence:
  13, 40, 20, 10, 5, 16, 8, 4, 2, 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import common

# By caching the chain lengths of all partial chains we've seen before, 
# further chains can be computed much faster.
# For a one-off, this wouldn't help, but if we're checking all starting points
# under 1M, this results in a ~20x speedup.
cache = {}

def threen(x):
  assert x > 0  # only defined on positive integers
  terms = [x]
  tail = 0
  while x != 1:
    if x in cache:
      tail = cache[x]
      break
    if x % 2:
      x = 3*x + 1
    else:
      x = x/2
    terms.append(x)
  for i,t in enumerate(terms):
    cache[t] = len(terms) - i + tail
  return len(terms) + tail

common.assertEquals(10, threen(13))

def euler014(limit):
  length, start = max((threen(i),i) for i in range(1,limit))
  #  print "(The path from %d to 1 contains %d term(s))" % (start, length)
  return start

common.assertEquals(9, euler014(10))

# alternate approach, turns out to be too slow:
def reverse_threen(limit):
  needed = set(range(2,limit))
  seen = set([1])
  distance = {1:set([1])}
  while needed:
    d = max(distance.keys())
    terms = distance[d]
    #print d, len(terms)
    newterms = set()
    for t in terms:
      if t*2 not in seen:
        newterms.add(t*2)
      if t%3 == 1 and t > 1 and t/3 % 2 and t/3 not in seen:
        newterms.add(t/3)
    for t in newterms:
      if t in needed: needed.remove(t)
      seen.add(t)
    distance[d+1] = newterms
  return max(t for t in distance[max(distance.keys())] if t < limit)

common.assertEquals(9, reverse_threen(10))

common.submit(euler014(10**6), expected=837799)
