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

# Find all the prime factors
def find_factors(n, start=2, factors=None):
    if factors is None:
        factors = defaultdict(int)
    if n == 1:
        return factors
    for i in xrange(start, n + 1):
        if is_prime(i) and n % i == 0:
            factors[i] += 1
            return find_factors(n / i, i, factors)
    return factors

a = int(raw_input())
if a == 1:
    x = {1: 1}
else:
    x = find_factors(a)


# [2] -> [2]
# [2, 2] -> [4]
# [2, 2, 2] -> [4, 2]
# [2, 2, 2, 2] -> [4, 4] -> [16] OR [8, 2]
# [2, 2, 2, 2, 2] -> [4, 4, 2] -> [16, 2] OR [8, 2, 2] -> [8, 4]
# [2, 2, 2, 2, 2, 2] -> [8, 4, 2]
# Ah-ha this is just triangular numbers
# Oh wait, this doesn't work for 36: [2 * 3 * 6] because we need to combine a 2 and a 3

print sum(x.values())
