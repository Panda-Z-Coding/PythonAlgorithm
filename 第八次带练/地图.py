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
    n, m, k = il()
    dp = [[[[0]*2 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    # i行j列，u次改变,v（0下1右）
    g = []
    for i in range(n):
        g.append(read())
    if n == 1 or m == 1:
        print(1)
        exit()
    for i in range(n):
        # 初始化第一行的点
        if g[i][0] != '#':
            dp[i][0][0][0] = 1
        else:
            break
    for i in range(m):
        # 初始化第一列的点
        if g[0][i] != '#':
            dp[0][i][0][1] = 1
        else:
            break
    for i in range(1,n):
        for j in range(1,m):
            if g[i][j] != '#':
                for u in range(k+1):
                    if i >= 1:
                        dp[i][j][u][0] = dp[i-1][j][u][0]
                        if u >= 1:
                            dp[i][j][u][0] = (dp[i][j][u][0] + dp[i-1][j][u-1][1]) % mod
                    if j >= 1:
                        dp[i][j][u][1] = dp[i][j-1][u][1]
                        if u >= 1:
                            dp[i][j][u][1] = (dp[i][j][u][1] + dp[i][j-1][u-1][0]) % mod
    ans = 0
    for i in range(k+1):
        for j in range(2):
            ans = (ans + dp[n-1][m-1][i][j]) % mod
    print(ans)

t = 1
for _ in range(t):
    solve()