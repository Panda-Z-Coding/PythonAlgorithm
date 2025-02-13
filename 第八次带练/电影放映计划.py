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
    m, n = il()
    t, p = [0]*n, [0]*n
    for i in range(n):
        t[i], p[i] = il()
    k = ii()
    m += k
    for i in range(n):
        t[i] += k
    dp = [0] * (m+1)
    for i in range(1, m+1):
        dp[i] = dp[i - 1]
        for j in range(n):
            if i >= t[j]:
                dp[i] = max(dp[i],dp[i-t[j]]+p[j])
    print(dp[m])

t = 1
for _ in range(t):
    solve()