N = int(raw_input())
for _ in xrange(N):
    n, source, target = raw_input().split()

    def get_map(language):
        m = {}
        c = 0
        for x in language:
            m[x] = c
            c += 1
        return m

    source_map, target_map = (get_map(x) for x in (source, target))
    inv_target_map = {v: k for k, v in target_map.iteritems()}

    # convert to a number value using the source map
    total = 0
    for x in n:
        total *= len(source)
        total += source_map[x]

    # Convert back to the target language using the inverted target map
    biggest = 1
    l = 0
    while biggest <= total:
        biggest *= len(target)
        l += 1
    biggest /= len(target)

    out = ""
    index = 0
    while total > 0 or index < l:
        n = total / biggest
        total -= n * biggest
        out += inv_target_map[n]
        biggest /= len(target)
        index += 1
    print "Case #%s: %s" % (_ + 1, out)
