import itertools
import collections

def assertEquals(expected, actual):
  if expected != actual:
    raise AssertionError("expected: %s;\tactual: %s" % (expected, actual))

assertEquals(0, 0)
try:
  assertEquals(1, 0)
  assert False
except AssertionError:
  pass

def submit(answer, expected=None):
  if expected is not None:
    assertEquals(expected, answer)
  print answer

def fibs():
  previous, current = 0, 1
  while True:
    yield previous
    previous, current = current, previous + current

assertEquals([0,1,1,2,3,5,8], list(itertools.islice(fibs(), 7)))

_cached_primes = [2,3]
def _generate_prime():
  for n in itertools.count(_cached_primes[-1] + 2, 2):
    for p in _cached_primes:
      if p*p > n:
        _cached_primes.append(n)
        return
      if n % p == 0:
        break

def nth_prime(n):
  if n < 0: raise IndexError
  while n >= len(_cached_primes):
    _generate_prime()
  return _cached_primes[n]

assertEquals(2, nth_prime(0))
assertEquals(3, nth_prime(1))
assertEquals(5, nth_prime(2))
assertEquals(7, nth_prime(3))
try:
  nth_prime(-1)
  assert False
except IndexError:
  pass

def primes():
  for i in itertools.count():
    yield nth_prime(i)

def factor(x):
  if x < 1: return None
  result = []
  for p in primes():
    while x % p == 0:
      x /= p
      result.append(p)
    if p*p > x:
      if x != 1:
        result.append(x)
      break
  return result

assertEquals(None, factor(0))
assertEquals([], factor(1))
assertEquals([2], factor(2)) 
assertEquals([3], factor(3)) 
assertEquals([2, 2], factor(4))
assertEquals([5], factor(5))
assertEquals([2, 3], factor(6))
assertEquals([2, 2, 2], factor(8))
assertEquals([2, 2, 3], factor(12))

def prime(x):
  if x < 2: return False
  for p in primes():
    if p*p > x: return True
    if x % p == 0: return False

assertEquals(True, prime(2))
assertEquals(True, prime(3))
assertEquals(False, prime(4))
assertEquals(True, prime(5))
assertEquals(False, prime(6))
assertEquals(True, prime(7))
assertEquals(False, prime(121))

import operator
def product(sequence):
  return reduce(operator.mul, sequence, 1)

def num_divisors(x):
  if not x: return 0
  return product([m+1 for m in collections.Counter(factor(x)).values()])

assertEquals(0, num_divisors(0))
assertEquals(1, num_divisors(1))
assertEquals(2, num_divisors(2))
assertEquals(2, num_divisors(3))
assertEquals(3, num_divisors(4))
assertEquals(4, num_divisors(6))
assertEquals(4, num_divisors(8))
assertEquals(6, num_divisors(12))
assertEquals(2, num_divisors(13))

def divisors(x):
  if not x: return []
  divisors = [1]
  for f, frequency in collections.Counter(factor(x)).iteritems():
    divisors2 = []
    for divisor in divisors:
      for i in range(frequency+1):
        divisors2.append(divisor * (f**i))
    divisors = divisors2
  divisors.sort()
  return divisors

assertEquals([], divisors(0))
assertEquals([1], divisors(1))
assertEquals([1, 2], divisors(2))
assertEquals([1, 3], divisors(3))
assertEquals([1, 2, 4], divisors(4))
assertEquals([1, 2, 3, 6], divisors(6))
assertEquals([1, 2, 4, 8], divisors(8))
assertEquals([1, 2, 3, 4, 6, 12], divisors(12))

def palindrome(x):
  string = str(x)
  return string == string[::-1]

assertEquals(True, palindrome(0))
assertEquals(True, palindrome(1))
assertEquals(False, palindrome(10))
assertEquals(True, palindrome(11))
assertEquals(True, palindrome(101))
assertEquals(False, palindrome(123))

def lettervalue(c):
  return ord(c) - ord('A') + 1

assertEquals(3, lettervalue('C'))
assertEquals(15, lettervalue('O'))
assertEquals(12, lettervalue('L'))
assertEquals(9, lettervalue('I'))
assertEquals(14, lettervalue('N'))

def wordvalue(w):
  return sum(lettervalue(c) for c in w)

assertEquals(53, wordvalue('COLIN'))

def c(n,r):
  return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

def gcd(a, b):
    while b:
       b, a = a % b, b
    return a

assertEquals(0, gcd(0, 0))
assertEquals(21, gcd(1071, 462))

def lcm(a, b):
    if not a or not b: return 0
    return a*b/gcd(a, b)

assertEquals(0, lcm(0, 0))
assertEquals(0, lcm(0, 5))
assertEquals(7, lcm(1, 7))
assertEquals(12, lcm(3, 4))
assertEquals(36, lcm(12, 18))

import collections
import functools
class memoized(object):
  '''Decorator. Caches a function's return value each time it is called.
  If called later with the same arguments, the cached value is returned
  (not reevaluated).

  Cribbed from https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
  '''
  def __init__(self, func):
    self.func = func
    self.cache = {}
  def __call__(self, *args):
    if not isinstance(args, collections.Hashable):
      # uncacheable. a list, for instance.
      # better to not cache than blow up.
      return self.func(*args)
    if args in self.cache:
      return self.cache[args]
    else:
      value = self.func(*args)
      self.cache[args] = value
      return value
  def __repr__(self):
    '''Return the function's docstring.'''
    return self.func.__doc__
  def __get__(self, obj, objtype):
    '''Support instance methods.'''
    return functools.partial(self.__call__, obj)


def fraction(n, d):
  if n >= d: return None
  seen_remainders = {}  # index at which that remainder was last seen
  remainder = n * 10
  result = []
  while remainder not in seen_remainders:
    seen_remainders[remainder] = len(result)
    result.append(remainder / d)
    remainder = remainder % d * 10
  last_seen = seen_remainders[remainder]
  return (result[:last_seen], result[last_seen:])

assertEquals(([5], [0]), fraction(1,2))
assertEquals(([],[3]), fraction(1,3))
assertEquals(([2,5], [0]), fraction(1,4))
assertEquals(([2], [0]), fraction(1,5))
assertEquals(([1], [6]), fraction(1,6))
assertEquals(([], [1,4,2,8,5,7]), fraction(1,7))
assertEquals(([1,2,5], [0]), fraction(1,8))
assertEquals(([], [1]), fraction(1,9))
assertEquals(([1], [0]), fraction(1,10))
assertEquals(([], [6]), fraction(2,3))
assertEquals(([5], [0]), fraction(49,98))
assertEquals(([5], [0]), fraction(4,8))
