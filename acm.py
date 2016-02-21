from collections import defaultdict

solves = {}
penalties = defaultdict(int)
while True:
    l = raw_input().split()
    if len(l) == 1 and l[0] == '-1':
        break
    t, prob, solved = int(l[0]), l[1], l[2] == "right"
    if solved:
        solves[prob] = penalties.get(prob, 0) + t
    else:
        penalties[prob] += 20
print "%s %s" % (len(solves), sum(solves.values()))
