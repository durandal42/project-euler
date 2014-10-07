'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''

import common
import itertools

useful_primes = set(
  p for p in itertools.takewhile(lambda x: x < 10**4,
                                 itertools.dropwhile(lambda x: x < 10**3,
                                                     common.primes())))

def euler049():
  for i in useful_primes:
    if i == 1487: continue  # skip known solution
    for j in useful_primes:
      if i >= j: continue
      if sorted(str(i)) != sorted(str(j)): continue
      k = j + (j - i)
      if k not in useful_primes: continue
      if sorted(str(i)) != sorted(str(k)): continue
      return int('%d%d%d' % (i,j,k))

common.submit(euler049(), expected=296962999629)
