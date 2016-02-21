import itertools

ops = ["*", "+", "-", "/"]
template = "4%s4%s4%s4"

def process_line(line):
    global ops, template
    n = int(line)
    to_try = itertools.product(ops, ops, ops)
    for tup in to_try:
        x = eval(template % tup)
        if x == n:
            return tup, x
    return None, None


n = int(raw_input())
for _ in range(n):
    tup, x = process_line(raw_input())
    if tup is None:
        print "no solution"
    else:
        print "4 %s 4 %s 4 %s 4 = %s" % (tup[0], tup[1], tup[2], x)
