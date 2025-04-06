import os
import sys
from collections import defaultdict
from queue import PriorityQueue
import math
# 先把这个图给构建出来, 然后dijk
def lcm(a, b):
    return a * b // math.gcd(a, b)

gp = defaultdict(list)
for i in range(1, 2021 + 1):
    for j in range(i, 2021 + 1):
        if j - i <= 21:
            t = lcm(i, j)
            gp[i].append((j, t))
            gp[j].append((i, t))

# dijk
q = PriorityQueue()
inf = float('inf')
d = [inf] * (2021 + 1)
d[1] = 0
q.put((0, 1))
vis = [False] * (2021 + 1)
while not q.empty():
    _, u = q.get()
    if vis[u]: continue
    vis[u] = True
    for v, w in gp[u]:
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            q.put((d[v], v))
print(d[2021])


