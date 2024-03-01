# pip install --no-build-isolation -v .

import nbtest
import time

s = nbtest.S()
xs = nbtest.XS()


def bench(s, N):
    s.clear()
    t0 = time.time()
    for i in range(N):
        s += i
    t1 = time.time()
    return t1 - t0


Ns = [10**i for i in range(2, 6)]

S_time = []
XS_time = []

for N in Ns:
    S_time.append(bench(s, N))
    XS_time.append(bench(xs, N))

# print result
for (i, N) in enumerate(Ns):
    print(f"N = {N}, \tS_time = {S_time[i]:.4f}, XS_time = {XS_time[i]:.4f}")
