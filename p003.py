'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import common
def largest_prime_factor(n):
    return common.factor(n)[-1]

common.assertEquals(29, largest_prime_factor(13195))

common.submit(largest_prime_factor(600851475143), expected=6857)

# command-line utility
import sys
for arg in sys.argv[1:]:
    print '%d = %s' % (
        int(arg), common.factor(int(arg)))
