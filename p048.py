'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

import common

# "last ten digits" = "give me the result mod 10**10"
# since addition and exponentiation work under modular arithmetic, just do
# all the work mod 10**10
def euler048(n, modulus=None):
  result = sum([pow(i, i, modulus) for i in range(1, n+1)])
  if modulus: result %= modulus
  return result

common.assertEquals(10405071317, euler048(10))

common.submit(euler048(1000, 10**10), expected=9110846700)
