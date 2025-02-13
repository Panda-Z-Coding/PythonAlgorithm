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
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(min(m+1,k+1)):
        # 第一条街，能建的所有房子数，都为初始值1
        dp[0][i] = 1
    for i in range(1, n):
        # 枚举接下来的街
        for j in range(1, m + 1):
            # 枚举第i+1条街，建造的房子数
            for l in range(i, k + 1 - j):
                # 前i条街已经建造房子数
                dp[i][j + l] += dp[i-1][l]
                dp[i][j + l] %= mod
    print(sum(dp[n-1][:k+1])%mod)

t = 1
for _ in range(t):
    solve()