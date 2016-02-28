from collections import deque
c = 1
while True:
    n = int(raw_input())
    if n == 0:
        break
    d = deque()
    l = []
    for _ in range(n):
        l.append(raw_input().strip())
    l.reverse()
    if n % 2 == 0:
        d.append(l[0])
        l = l[1:]
    for i, n in enumerate(l):
        if not i % 2:
            d.appendleft(n)
        else:
            d.append(n)
    print "SET %s" % (c)
    for s in d:
        print s
    c += 1
