n, q = (int(x) for x in raw_input().strip().split())
tree = [0 for x in xrange(n + 1)]

def update(index, v):
    while index <= n:
        tree[index] += v
        index += (index & -index)

def read(index):
    s = 0
    while index > 0:
        s += tree[index]
        index -= (index & -index)
    return s

for _ in xrange(q):
    command = raw_input().split()
    if command[0] == "?":
        print read(int(command[-1]))
    else:
        update(int(command[-2]) + 1, int(command[-1]))
