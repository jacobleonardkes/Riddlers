import numpy as np
from fractions import Fraction as F

cache = {}

def P(n, m):
    if (n, m) not in cache:
        if n == 1:
            cache[n, m] = F(1)
        elif m == 1:
            cache[n, m] = F(1, n)
        else:
            best = F(1, n) + ((n-F(1))/n) * (F(1) - P(m, n-1))
            for i in range(2, n-1):
                thisP = F(i, n)*(F(1)-P(m, i)) + F(n-i, n)*(F(1)-P(m, n-i))
                best = max(best, thisP)
            cache[n, m] = best
    return cache[n, m]

print('P(4,4)=%s' % P(4, 4))
print('P(14,14)=%s' % P(14, 14))
print('P(24,24)=%s' % P(24, 24))

print('Table:')
print('n\\m | ' + ' | '.join(['%5d' % m for m in range(1, 25)]))
for n in range(1, 25):
    print('%3d | ' % n + ' | '.join(['%.3f' % P(n, m) for m in range(1, 25)]))
