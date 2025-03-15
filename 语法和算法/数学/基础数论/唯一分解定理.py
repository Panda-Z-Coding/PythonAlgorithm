import os
import sys

from collections import Counter

def f(n):
    factor = []
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            factor.append(i)
        if n == 1:
            break
    return factor

all_factor = []
for i in range(2, 101):
    all_factor += f(i)

all_factor = Counter(all_factor)
ans = 1
for p in all_factor.values():
    ans *= p + 1

print(ans)