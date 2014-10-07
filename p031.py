'''
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can L2 be made using any number of coins?
'''

import common

denominations = [1,2,5,10,20,50,100,200]
cache = {}

@common.memoized
def makechange(target, min):
  '''How many ways can we make change for 'total', using only denominations with index 'min' or higher?'''
  if min >= len(denominations) and target > 0: return 0
  if target == 0: return 1
  return sum(makechange(target - denominations[min]*c, min+1)
             for c in range(1 + target / denominations[min]))

common.submit(makechange(200, 0), expected=73682)
