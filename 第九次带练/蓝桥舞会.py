import sys
import math
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
    n = ii()
    a = [0] + il()
    g = [[] for _ in range(n + 1)]
    for i in range(n-1):
        u, v = il()
        g[v].append(u)
    dp = [[0] * 2 for _ in range(n+1)]
    def dfs(u):
        dp[u][1] = a[u]
        for v in g[u]:
            dfs(v)
            dp[u][1] += dp[v][0]
            dp[u][0] += max(dp[v][1],dp[v][0])
    dfs(1)
    print(max(dp[1]))

t = 1
for _ in range(t):
    solve()