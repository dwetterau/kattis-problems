n = int(raw_input())
ns = set()
for _ in range(n):
    ns.add(int(raw_input()))
m = int(raw_input())
ms = []
for _ in range(m):
    ms.append(int(raw_input()))

# Now build s from ns.
s = [0 if x not in ns else 1 for x in range(2 * max(ns) + 1)]
s2 = s[::1]
s2[0] = 1

# It's FFT time
def next_power_of_2(n):
    cur = 1
    while cur < n:
        cur <<= 1
    return cur

import cmath

def fft(array, inverse=False):
    # Pad the input to be a power of 2 length
    l = next_power_of_2(len(array))
    new_array = []
    for i in range(l):
        if i < len(array):
            new_array.append(array[i])
        else:
            new_array.append(0)

    def _fft(a):
        n = len(a)
        if n == 1:
            return a
        w_n = cmath.exp((2 * cmath.pi * 1j) / n)
        if inverse:
            w_n = 1 / w_n

        w = complex(1.0)
        a_0 = [x for i, x in enumerate(a) if i % 2 == 0]
        a_1 = [x for i, x in enumerate(a) if i % 2 == 1]
        y_0, y_1 = _fft(a_0), _fft(a_1)
        y = [0 for _ in a]
        half_n = n / 2
        for k in range(half_n):
            rhs = w * y_1[k]
            y[k] = y_0[k] + rhs
            y[k + half_n] = y_0[k] - rhs
            w *= w_n
        return y
    ret = _fft(new_array)
    if inverse:
        ret = [x / float(l) for x in ret]
    return ret

# Alright, lets use that bad boy
A = fft(s)
B = fft(s2)
assert len(A) == len(B)
C = [A[i] * B[i] for i in range(len(A))]
c = fft(C, inverse=True)

# Clean up C and throw it in a set
values = set()
for i, v in enumerate(c):
    if round(v.real) > 0:
        values.add(i)

print sum(1 for x in ms if x in values)
