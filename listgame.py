import math
from collections import defaultdict

import sys

m = {}
# Computes if something is prime
def is_prime(x):
    if x == 2 or x == 3: return True
    if x < 2 or x % 2 == 0: return False
    if x < 9: return True
    if x % 3 == 0: return False
    if x in m:
        return m[x]
    f = 5
    r = math.sqrt(x)
    while f <= r:
        if x % f == 0 or x % (f + 2) == 0:
            m[x] = False
            return False
        f += 6
    m[x] = True
    return True

a = int(raw_input())
if a == 1:
    x = {1: 1}
else:
    x = defaultdict(int)
    limit = int(math.sqrt(a)) + 1
    for i in xrange(2, limit):
        if i == a:
            break
        if is_prime(i):
            while a % i == 0 and i != a:
                a /= i
                x[i] += 1
        if i == a:
            break

print sum(x.values()) + 1
