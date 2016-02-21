n = int(raw_input())
for _ in range(n):
    raw_input()
    n1, n2 = raw_input().split(" ")
    army1 = [int(x) for x in raw_input().split(" ")]
    army2 = [int(x) for x in raw_input().split(" ")]
    army1.sort()
    army2.sort()
    a1 = 0
    a2 = 0

    while a1 < len(army1) and a2 < len(army2):
        if army1[a1] < army2[a2]:
            # Mecha won
            a1 += 1
        elif army1[a1] > army2[a2]:
            # God won
            a2 += 1
        else:
            # Mecha loses ties
            a2 += 1
    winner = 1 if a1 == len(army1) else 0
    print "Godzilla" if winner == 0 else "MechaGodzilla"
