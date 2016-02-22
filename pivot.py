import math
from collections import defaultdict

import sys

n = int(raw_input())
a = [int(x) for x in raw_input().split()]
s = []

# Pass left to right
for x in a:
    while s and s[-1] > x:
        s.pop()
    s.append(x)
lhs = set(s)
s = []
for x in a[::-1]:
    while s and s[-1] < x:
        s.pop()
    s.append(x)
rhs = set(s)
print len(lhs & rhs)
