import math
from collections import defaultdict

import sys

best, best_index = 0, -1
for i in range(5):
    s = sum(int(x) for x in raw_input().split())
    if s > best:
        best_index = i
        best = s

print "%s %s" % (best_index + 1, best)
