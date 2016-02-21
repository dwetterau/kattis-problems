from math import factorial, log

m, n, t = (int(x) for x in raw_input().split())

funcs = {
    1: lambda x: factorial(x),
    2: lambda x: 2**x,
    3: lambda x: x * x * x * x,
    4: lambda x: x * x * x,
    5: lambda x: x * x,
    6: lambda x: x * log(x, 2),
    7: lambda x: x,
}

# Pre-filters
filters = {
    1: 13,
    2: 30,
    3: 178,
    4: 1001,
    5: 31623,
    6: 100000000,
    7: 1e9 + 1,
}
if filters[t] <= n:
    print "TLE"
else:
    if funcs[t](n) <= m:
        print "AC"
    else:
        print "TLE"
