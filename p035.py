'''
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import common

def circular(n):
  s = str(n)

  if len(s) > 1:
    for c in s:
      if c not in ['1', '3', '7', '9']:
        return False

  for i in range(len(s)):
    if not common.prime(int(s[i:] + s[:i])):
      return False

  return True

def euler035(limit):
  return len([i for i in range(limit) if circular(i)])

common.assertEquals(13, euler035(100))

common.submit(euler035(10**6), expected=55)
