from itertools import chain, combinations

m = dict()
def all_subsets(l):
    return chain.from_iterable(combinations(l, n) for n in range(1, len(l) + 1))

t = int(raw_input())

for case in range(t):
    print "Case #%s:" % (case + 1)
    l = [int(x) for x in raw_input().split()]
    n = l[0]
    l = l[1:]
    subsets = all_subsets(l)
    for s in subsets:
        su = sum(s)
        if su in m:
            print " ".join(str(x) for x in m[su])
            print " ".join(str(x) for x in s)
            break
        m[su] = s
    else:
        print "Impossible"