'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

NOTE(durandal): the auto-grader seems to want the *index* of the first such term; in the baby example, the correct answer would be 12, not 144.
'''

import common

def euler025(digits):
  for i,f in enumerate(common.fibs()):
    if len(str(f)) >= digits:
      return i

common.assertEquals(12, euler025(3))

common.submit(euler025(1000), expected=4782)
