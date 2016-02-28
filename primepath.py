import collections
import math

n = 10000
sieve = [True for _ in xrange(n // 2 + 1)]

limit = int(math.sqrt(n))
size = n // 2 + 1
for i in xrange(1, limit):
    if sieve[i]:
        val = 2 * i + 1
        temp = ((size - 1) - i) // val
        sieve[i + val::val] = [False] * temp

def is_prime(x):
    if x % 2 == 0 or not is_valid(x):
        return False
    else:
        return sieve[x // 2]

def is_valid(x):
    return x >= 1000 and x <= 9999

nodes = dict()
for x in xrange(1000, 10000):
    if is_prime(x):
        s = {x}
        for f in [1, 10, 100, 1000]:
            place = (x % (f * 10)) // f
            xr = x - place * f
            for y in [z for z in range(10) if z != place]:
                t = xr + (y * f)
                if is_prime(t):
                    s.add(t)
        nodes[x] = s

# Now we just have to traverse for each input
n = int(raw_input())
for _ in xrange(n):
    start, end = (int(x) for x in raw_input().split())
    q = collections.deque()
    q.append((start, 0))
    seen = set()
    while q:
        s, d = q.popleft()
        if s == end:
            print d
            break
        if s in seen:
            continue
        seen.add(s)
        for x in nodes[s]:
            if x not in seen:
                q.append((x, d + 1))
    else:
        print "impossible"