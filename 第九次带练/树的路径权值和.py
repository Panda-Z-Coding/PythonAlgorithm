import sys
import math
import collections
from functools import cmp_to_key
from sys import exit
sys.setrecursionlimit(1000000)  # 设置新的递归深度限制

def read():
    return sys.stdin.readline().strip()

def ii():
    return int(read())

def il():
    return list(map(int,read().split()))
N = 100010
M = N * 2
mod = 1000000007
inf = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = []

def solve():
    n = ii()
    g = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u, v = il()
        g[u].append(v)
        g[v].append(u)
    w = [0]
    for _ in range(n):
        w.append(ii())
    dis1 = [0] * (n + 1)
    dis2 = [0] * (n + 1)
    p1 = [0] * (n + 1)
    p2 = [0] * (n + 1)
    def dfs1(u, pa):
        dis1[u] = w[u]
        for v in g[u]:
            if v != pa:
                dfs1(v, u)
                t = dis1[v] + w[u]
                if t > dis1[u]:
                    p2[u] = p1[u]
                    p1[u] = v
                    dis2[u] = dis1[u]
                    dis1[u] = t
                elif t > dis2[u]:
                    p2[u] = v
                    dis2[u] = t
    dfs1(1, -1)
    up = [0] * (n + 1)
    def dfs2(u, pa):
        for v in g[u]:
            if v != pa:
                if v != p1[u]:
                    up[v] = max(dis1[u], up[u]) + w[v]
                else:
                    up[v] = max(dis2[u], up[u]) + w[v]
                dfs2(v, u)
    dfs2(1, -1)
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, dis1[i] + dis2[i] - w[i], dis1[i] + up[i] - w[i])
    print(ans)


t = 1
for _ in range(t):
    solve()