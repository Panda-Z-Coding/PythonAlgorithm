import os
import sys
input = sys.stdin.readline
from queue import PriorityQueue
from collections import defaultdict
def topo():
    q = PriorityQueue()
    ans = []
    for i in range(1, n + 1):
        if ru[i] == 0:
            q.put(i)
    while not q.empty():
        u = q.get()
        ans.append(u)
        for v in G[u]:
            ru[v] -= 1
            if ru[v] == 0:
                q.put(v)
    if len(ans) == n:
        print(*ans)
    else:
        print(-1)

n, m = map(int, input().split())
G = defaultdict(list)
ru = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    ru[v] += 1
    G[u].append(v)

topo()
