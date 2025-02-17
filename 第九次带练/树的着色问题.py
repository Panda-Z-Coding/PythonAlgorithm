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
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = il()
        g[u].append(v)
        g[v].append(u)
    dp = [[0]*2 for _ in range(n+1)]
    def dfs(u,pa):
        dp[u][0], dp[u][1] = 1, 1
        for v in g[u]:
            if v == pa:
                continue
            dfs(v,u)
            dp[u][0] *= dp[v][1] + dp[v][0]
            dp[u][0] %= mod
            dp[u][1] *= dp[v][0]
            dp[u][1] %= mod
    dfs(1,-1)
    print(sum(dp[1])%mod)

t = 1
for _ in range(t):
    solve()