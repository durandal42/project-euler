'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by
1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated
product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import common
import itertools

def pandigital(s):
  return sorted(s) == ['1','2','3','4','5','6','7','8','9'][:len(s)]

common.assertEquals(True, pandigital('1'))
common.assertEquals(False, pandigital('5'))
common.assertEquals(True, pandigital('123456789'))
common.assertEquals(True, pandigital('987654321'))
common.assertEquals(False, pandigital('112233445'))

def concatenated_product(n):
  string = ''
  for i in itertools.count(1):
    string += str(n * i)
    if len(string) >= 9: break
  if i > 1 and pandigital(string):
    # print n, range(1, i+1), string
    return int(string)
  else: return None

common.assertEquals(192384576, concatenated_product(192))
common.assertEquals(918273645, concatenated_product(9))

result = max(concatenated_product(i) for i in xrange(1,10**4))

common.submit(result, expected=932718654)
