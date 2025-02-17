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
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = []

def solve():
    n, m = il()
    g = [[] for _ in range(n + 1)]
    pa = [0] * (n + 1)
    for i in range(n-1):
        u, v = il()
        g[v].append(u)
        pa[u] = v
    cnt = [0] * (n + 1)
    def dfs(u):
        cnt[u] = 1
        for v in g[u]:
            cnt[u] += dfs(v)
        return cnt[u]
    rt = 1
    while pa[rt]:
        rt += 1
    dfs(rt)
    a = []
    for k, v in enumerate(cnt[1:]):
        # v是对应的节点数，k是节点编号
        a.append([v, k])
    a.sort(key=lambda x:(-x[0], x[1]))
    ans = 1
    for k, i in enumerate(a):
        if i[1] == m - 1:
            ans = k + 1
            break
    print(ans)
    

t = 1
for _ in range(t):
    solve()