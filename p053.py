import common

count = 0
for n in xrange(1, 101):
  for r in xrange(0, n+1):
    if common.c(n,r) > 1000000:
      count += 1
print count
