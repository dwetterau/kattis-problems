import fileinput
import math
from collections import defaultdict


def num_combinations(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

for line in fileinput.input():
    counts = defaultdict(int)
    for y in line.strip():
        counts[y] += 1
    total = 1
    n = sum(counts.values())
    i = 0
    all_counts = counts.values()
    while n > 0:
        total *= num_combinations(n, all_counts[i])
        n -= all_counts[i]
        i += 1
    print total
