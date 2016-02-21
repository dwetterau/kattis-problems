import math
from collections import defaultdict

m = {}
# Computes if something is prime
def is_prime(x):
    global m
    if x in m:
        return m[x]
    for i in xrange(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            m[x] = False
            return False
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

total = 0
last = -1
for factor, count in x.items():
    if count == 1:
        total += 1
        continue

    c, d, i = 1, 1, 1
    while d < count:
        d += i
        c += 1
        i += 1
    total += max(1, i - 2)

print total
