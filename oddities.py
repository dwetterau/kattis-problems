import math
from collections import defaultdict

import sys

n = int(raw_input())
for _ in xrange(n):
    x = int(raw_input())
    print "%s is %s" % (x, "even" if x % 2 == 0 else "odd")
