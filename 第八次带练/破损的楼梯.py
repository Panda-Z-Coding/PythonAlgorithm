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
    n, m = il()
    b = [0] * (n + 1)
    a = il()
    for x in a:
        b[x] = 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if not b[i-1]:
            dp[i] = dp[i-1]
        if i >= 2 and not b[i-2]:
            dp[i] = (dp[i] + dp[i-2]) % mod
    print(dp[n])

t = 1
for _ in range(t):
    solve()