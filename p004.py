'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import common
import heapq


def euler004_brute(digits):
  return max(i * j
             for i in range(10**(digits - 1), 10**digits)
             for j in range(i, 10**digits)
             if common.palindrome(i * j))


def euler004_queue(digits):
  checked = set()
  todo = []
  max = 10**digits - 1
  heapq.heappush(todo, (-max * max, max, max))
  while todo:
    negative_product, i, j = heapq.heappop(todo)
    if (i, j) in checked:
      continue
    checked.add((i, j))
    if common.palindrome(-negative_product):
      return -negative_product
    heapq.heappush(todo, (-(i - 1) * j, i - 1, j))
    heapq.heappush(todo, (-i * (j - 1), i, j - 1))

euler004 = euler004_queue

common.assertEquals(9009, euler004(2))
common.submit(euler004(3), expected=906609)
