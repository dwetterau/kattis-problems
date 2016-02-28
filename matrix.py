try:
    c = 1
    while True:
        mat = [[int(x) for x in raw_input().split()] for _ in range(2)]
        det = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        mat[0][0], mat[1][1] = mat[1][1], mat[0][0]
        mat[0][1] = -mat[0][1]
        mat[1][0] = -mat[1][0]
        print "Case %s:" % c
        for r in range(2):
            print "%s %s" % tuple(mat[r][x] / det for x in range(2))
        raw_input()
        c += 1
except EOFError:
    pass

