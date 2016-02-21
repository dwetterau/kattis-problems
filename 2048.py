
lines = [[] for x in range(4)]
for i in range(4):
    lines[i] = [int(x) for x in raw_input().split(" ")]
move = int(raw_input())

if move == 3:
    # Down move
    for c in range(4):
        for r in range(4)[::-1]:
            if r == 0:
                break
            while lines[r][c] == 0:
                lines[0][c] = 0
                for i in range(1, 4)[::-1]:
                    pass

elif move == 1:
    # Up move
    pass
elif move == 2:
    # Right move
    pass
else:
    # Left move
    pass
