'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import common

def cancels(n1, d1, n2, d2):
  left = common.fraction(n1, d1) 
  right = common.fraction(n2, d2)
  return left == right and left is not None

common.assertEquals(True, cancels(49,98, 4,8))

n = 1
d = 1
for a in range(10):
  for b in range(10):
    for c in range(1,10):
      if cancels(10*a + c, b + 10*c, a, b):
        print '%d%d/%d%d = %d/%d' %(a,c,c,b,a,b)
        n *= a
        d *= b
          
print '%d/%d' % (n,d)

gcd = common.gcd(n,d)
n /= gcd
d /= gcd

print '%d/%d' % (n,d)

common.submit(d, expected=100)
