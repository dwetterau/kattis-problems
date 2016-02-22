import math

n, q = (int(x) for x in raw_input().split())
sieve = [True for _ in xrange(n // 2 + 1)]

limit = int(math.sqrt(n))
size = n // 2 + 1
for i in xrange(1, limit):
    if sieve[i]:
        val = 2 * i + 1
        temp = ((size - 1) - i) // val
        sieve[i + val::val] = [False] * temp

print sum(sieve)
for _ in xrange(q):
    x = int(raw_input())
    if x == 1:
        print "0"
    elif x % 2 == 0:
        print "1" if x == 2 else "0"
    else:
        print "1" if sieve[x // 2] else "0"
