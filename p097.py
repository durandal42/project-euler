'''
The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 2^6972593-1; it contains exactly 2,098,960
digits. Subsequently other Mersenne primes, of the form 2^p-1, have been found
which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433*2^7830457+1.

Find the last ten digits of this prime number.
'''

import common

# pow(b, e, m) returns b**e % m
# With m a power of 10, we can extract trailing digits.
MODULUS = 10**10  
common.submit((28433 * pow(2, 7830457, MODULUS) + 1) % MODULUS,
              expected=8739992577)
