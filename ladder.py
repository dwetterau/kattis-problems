import math
h, d = (int(x) for x in raw_input().split())
print int(math.ceil(h / math.sin(d * math.pi / 180)))