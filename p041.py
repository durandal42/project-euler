'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''

import common
import itertools  

def pandigitals():
  return itertools.chain.from_iterable(
    map(lambda p: int(''.join(p)),
        itertools.permutations('123456789'[:d]))
    for d in range(1,10))

result = max(filter(common.prime, pandigitals()))

common.submit(result, expected=7652413)
