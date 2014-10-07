def digits(x):
  result = [int(d) for d in str(x)]
  result.sort()
  return result

i = 0
while True:
  i += 1
  d = digits(i)
  if d == digits(2*i) and d == digits(3*i) and d == digits(4*i) and d == digits(5*i) and d == digits(6*i):
    print i
    break
