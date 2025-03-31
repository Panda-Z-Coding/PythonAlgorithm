import os
import sys
input = sys.stdin.readline
from queue import PriorityQueue
from collections import defaultdict
# Dijk也不就是BFS+优先队列吗

n, m = map(int, input().split())
G = defaultdict(list)
for i in range(m):
    u, v, w = map(int, input().split())
    G[u].append((v, w)) # 从 u -> v 距离为w

inf = float('inf')
def dijk(s): # 从s算到所有点的最短距离
    d = [inf] * (n + 1) # d[i] 从s出发到i的最短距离
    # 记得初始化
    d[s] = 0
    vis = [False] * (n + 1) # 这个是看是否已经出过队列
    q = PriorityQueue()
    q.put((d[s], s)) # 第一个元素为优先级
    while not q.empty():
        _, u = q.get() # 只需要知道当前位置
        # 出队列就打标记
        if vis[u]: continue
        vis[u] = True
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                q.put((d[v], v))
    for i in range(1, n + 1):
        if d[i] == inf:
            d[i] = -1
    return d[1::] # 从1开始



print(*dijk(1))