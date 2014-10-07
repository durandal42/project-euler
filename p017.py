'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
'''

import common

def pronounce(x):
  if x == 0:
    return ""
  if x <= 19:
    return { 1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
             6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
             11:"eleven", 12:"twelve", 13:"thirteen",
             14:"fourteen", 15:"fifteen", 16:"sixteen",
             17:"seventeen", 18:"eighteen", 19:"nineteen" }[x]
  if x < 100:
    return { 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty",
             6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety" }[x/10] + pronounce(x % 10)
  if x < 1000:
    if x%100:
      return pronounce(x/100) + "hundredand" + pronounce(x % 100)
    else:
      return pronounce(x/100) + "hundred"
  return "onethousand"

def letters_used(x):
  return len(pronounce(x))

common.assertEquals(23, letters_used(342))
common.assertEquals(20, letters_used(115))

def euler017(limit):
  return sum(letters_used(i) for i in range(1, limit+1))

common.assertEquals(19, euler017(5))

common.submit(euler017(1000), expected=21124)
