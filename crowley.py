import common
import operator
import Queue
import collections
import math
import fractions

def factors(n):
  # assert isinstance(n, tuple)
  return common.product(c+1 for c in n)

assert factors((1,)) == 2  # 1,2
assert factors((2,)) == 3  # 1,2,4

def value(n):
  # assert isinstance(n, tuple)
  return common.product(p**c for p,c in zip(common.primes(), n))  

assert value((1,)) == 2
assert value((2,)) == 4

def steps(n):
  # assert isinstance(n, tuple)
  result = []
  for i,c in enumerate(n):
    if i > 0 and n[i] >= n[i-1]: continue
    new = list(n)
    new[i] += 1
    result.append(tuple(new))
  result.append(n + (1,))
  return result

def display(n):
  return '%d = %s ~= 2^%d (%d factors)' % (value(n), n, math.log(value(n), 2), factors(n))
  # ' * '.join('%d**%d' % (prime,power) for prime, power in zip(common.primes(), n))

def special_factors(n, cap):
  v = value(n)
  factors = common.factor(v)
  return len([None for i,p in enumerate(factors)
              if common.product(factors[:i]) < cap and
              common.product(factors[i:]) < cap])

def concise_factors(factors):
  result = []
  for p in common.primes():
    assert p <= factors[0]
    result.append(0)
    while factors and factors[0] == p:
      result[-1] += 1
      factors.pop(0)
    if not factors: return tuple(result)

print 360
print common.factor(360)
print concise_factors(common.factor(360))
print special_factors(concise_factors(common.factor(360)), 100)

def f(k):
  print 'searching for value <= %d with most factors...' % k
  start = (1,)
  best = (factors(start), -value(start), start)
  #frontier = Queue.PriorityQueue()
  frontier = Queue.Queue()
  frontier.put((value(start), start))
  seen = set()
  seen.add(start)
  while not frontier.empty():
    _, current = frontier.get()
    #print 'considering: %d (%d factors): ' % (value(current), factors(current))
    seen.add(current)
    compare = (factors(current), -value(current), current)
    if compare > best:
      best = compare
      print 'new best:', display(current)
      print 'frontier, seen sizes:' , frontier.qsize(), len(seen)
    # elif value(current) <= value(best) and factors(current) >= factors(best):
    #   best = current
    #   print 'new best:', display(best)
    #   print 'frontier, seen sizes:' , frontier.qsize(), len(seen)
    for s in steps(current):
      vs = value(s)
      if s not in seen and vs <= k:
        seen.add(s)
        #print 'adding to frontier: %d' % value(s)
        frontier.put((vs, s))
  print 'best:', display(best[-1])
  return value(best[-1])

#print f(100)
#print f(107207100)
print f(2**128)
#print f(2**64)

'''
def f(k):
  v = collections.Counter()
  for i in range(1, k):
    for j in range(1, k):
      v[i*j] += 1
  print v.most_common(10)
  return v.most_common(1)[0][0]
print f(100)
print common.factor(f(100))
'''

'''
best128 = 216322257708313439598055454574159900000
print best128, concise_factors(common.factor(best128))
for s in steps(concise_factors(common.factor(best128))):
  print 'step:', s
alt_best128 = best128 / 83 * 49 * 2
print alt_best128
alt_best128_factors = common.factor(alt_best128)
print alt_best128_factors
print factors(concise_factors(alt_best128_factors))
print alt_best128 < 2**128
print 2**128
'''
