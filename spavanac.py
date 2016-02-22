import math
from collections import defaultdict

import sys

h, m = (int(x) for x in raw_input().split())
h += 24
m += 15
if m < 60:
    h -= 1
print "%s %s" % (h % 24, m % 60)
