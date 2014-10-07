'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

import common
import itertools

possible_products = set()
for perm in itertools.permutations('123456789'):
  # products must be exactly 4 digits long;
  # 3-digit products require 6 digits in the multipliers,
  #   and no 6-digit split can produce a product with as few as 3 digits
  # 5-digit products require 4 digits in the multipliers,
  #   and no 4-digit split can produce a product with as many as 5 digits
  product = int(''.join(perm[5:]))

  # the 5 digits on the left can be split 1-4,2-3; 3-2 and 4-1 are symmetrical.
  for split in [1,2]:
    if int(''.join(perm[:split]))*int(''.join(perm[split:5])) == product:
      possible_products.add(product)

common.submit(sum(possible_products), expected=45228)
