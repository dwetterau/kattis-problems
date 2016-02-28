t = int(raw_input())

for case in range(t):
    n = int(raw_input())
    s = set()
    for _ in range(n):
        s.add(raw_input().strip())
    print len(s)