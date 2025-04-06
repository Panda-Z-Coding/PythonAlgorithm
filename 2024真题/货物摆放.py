import os
import sys

# py写一次
# 先求出因子
n = 2021041820210418
i = 1
ac = []
while i * i < n:
    if n % i == 0:
        ac.append(i)
        if i != n // i:
            ac.append(n // i)
    i += 1
l = len(ac)
cnt = 0
for i in range(l):
    for j in range(l):
        if ac[i] * ac[j] > n: continue
        for k in range(l):
            if ac[i] * ac[j] * ac[k] == n:
                cnt += 1


print(cnt)
