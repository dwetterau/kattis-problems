cases = int(raw_input())
for c in xrange(cases):
    w, h, shots = (int(x) for x in raw_input().split())
    boards = []
    for x in range(2):
        boards.append([])
        b = boards[-1]
        for r in range(h):
            row = raw_input().strip()
            row = [x == "#" for x in row]
            b.append(row)
    winner = None
    player = 0
    playing = True
    p1_empty, p2_empty = False, False
    if all(all(x == False for x in boards[0][y]) for y in range(h)):
        p1_empty = True
    if all(all(x == False for x in boards[1][y]) for y in range(h)):
        p2_empty = True
    if p1_empty and not p2_empty:
        winner = "two"
    elif p2_empty and not p1_empty:
        winner = "one"
    elif p1_empty and p2_empty:
        winner = "draw"

    for shot in xrange(shots):
        if not playing:
            raw_input()
            continue
        x, y = (int(x) for x in raw_input().split())
        i = (player + 1) % 2
        if boards[i][h - y - 1][x]:
            # A hit! This player continues
            boards[i][h - y - 1][x] = False

            # Check for a winner
            if all(all(x == False for x in boards[i][y]) for y in range(h)):
                if winner is not None:
                    winner = "draw"
                    playing = False
                else:
                    winner = "one" if not player % 2 else "two"
                    # This player sunk all of the other player's ships, but they get one more turn
                    player = (player + 1) % 2
        else:
            if winner is not None:
                # This player missed, and another player had sunk all.
                playing = False
            player = (player + 1) % 2

    if winner is None or winner == "draw":
        print "draw"
    else:
        print "player %s wins" % winner

