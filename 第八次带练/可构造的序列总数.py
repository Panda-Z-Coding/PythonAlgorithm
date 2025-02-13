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
    k, n = il()
    dp = [[0] * (k+1) for _ in range(n)]
    for i in range(1, k+1):
        # 第1个位置，a1 = i
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(1, k+1):
            # j枚举的是dp[i-1][j]
            res = j
            while res <= k:
                dp[i][res] = (dp[i][res] + dp[i-1][j]) % mod
                res += j
    print(sum(dp[n-1][1:k+1])%mod)

t = 1
for _ in range(t):
    solve()