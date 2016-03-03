while True:
    n = int(raw_input())
    if n == -1:
        break
    t = 0
    time = 0
    for _ in xrange(n):
        x, dt = (int(x) for x in raw_input().split())
        t += x * (dt - time)
        time = dt
    print "%s miles" % t
