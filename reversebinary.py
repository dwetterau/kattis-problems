import math
from collections import defaultdict

import sys

n = int(raw_input())
s = 0
while n > 0:
    if n & 1 == 1:
        s += 1
    s <<= 1
    n >>= 1
print s >> 1
