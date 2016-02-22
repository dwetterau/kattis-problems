import math
from collections import defaultdict

import sys

n = int(raw_input())
ts = sorted((int(x) for x in raw_input().split()), reverse=True)
# Simulate the planting of trees
day = 1
max_day = 0
for t in ts:
    max_day = max(max_day, day + t)
    day += 1

print max_day + 1
