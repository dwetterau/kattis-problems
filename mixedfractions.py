import math
from collections import defaultdict

import sys

while True:
    n, d = (int(x) for x in raw_input().split())
    if d == 0:
        break
    print "%s %s / %s" % (n / d, n - ((n / d) * d), d)
