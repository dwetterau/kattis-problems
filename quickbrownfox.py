n = int(raw_input())
for _ in xrange(n):
    missing = set(x for x in "abcdefghijklmnopqrstuvwxyz")
    x = raw_input().strip().lower()
    for y in x:
        try:
            missing.remove(y)
        except KeyError:
            pass
    if missing:
        print "missing %s" % "".join(sorted(missing))
    else:
        print "pangram"
