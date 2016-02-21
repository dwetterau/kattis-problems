s = raw_input().strip()
c = 0
m = "PER"
for i, x in enumerate(s):
    if x != m[i % 3]:
        c += 1
print c