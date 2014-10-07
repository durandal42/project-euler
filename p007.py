'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import common

def euler007(n):
    return common.nth_prime(n-1)  # nth_prime is 0-indexed

common.assertEquals(13, euler007(6))

common.submit(euler007(10001), expected=104743)
