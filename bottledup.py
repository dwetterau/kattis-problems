s, v1, v2 = (int(x) for x in raw_input().split())
def foo(n):
    global v1, v2
    # First try using as many of v1 as possible but make sure to leave a multiple of v2 leftover
    n1 = n / v1
    left = n - (n1 * v1)
    if left == 0:
        return "%s %s" % (n1, 0)
    else:
        while n1 > 0 and left % v2 != 0:
            n1 -= 1
            left = n - (n1 * v1)
        if n1 == 0:
            # Couldn't use v1, have to only use v2
            if n % v2 == 0:
                return "%s %s" % (0, n / v2)
            else:
                return "Impossible"
        else:
            # We can use a mix of both!
            return "%s %s" % (n1, left / v2)
print foo(s)
