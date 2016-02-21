import fileinput
from math import sqrt, acos, pi


def process_line(line):
    r, x, y = (float(x) for x in line.split())
    if x*x + y*y >= r*r:
        return "miss"

    t = sqrt((r*r / (x*x + y*y)) - 1)

    xt, yt = x - t*y, y + t*x
    d1, d2 = sqrt(x*x + y*y), sqrt((yt - y)**2 + (xt - x)**2)

    theta = acos(d1 / r)
    a1, a2 = d1 * d2, theta * r*r
    a = pi * r*r
    return "%f %f" % tuple(sorted((a - (a2 - a1), a2 - a1))[::-1])

for line in fileinput.input():
    print process_line(line)
