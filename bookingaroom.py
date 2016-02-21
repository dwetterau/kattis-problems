r, n = (int(x) for x in raw_input().split())
target = 0
a = [True for x in range(r)]
for _ in range(n):
    room = int(raw_input())
    a[room - 1] = False
    if target == room - 1 and target < r:
        # Look for the next room
        while target < r and not a[target]:
            target += 1

if target < r:
    print target + 1
else:
    print "too late"
