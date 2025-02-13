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
    a = []
    for i in range(n):
        c, d, w = il()
        a.append({'c':c, 'd':d, 'w':w})
    a = [0] + sorted(a, key = lambda x:(x['d'], x['w']))
    dp = [0]*(100010)
    for i in range(1, n + 1):
        for j in range(a[i]['d'],a[i]['c']-1,-1):
                dp[j] = max(dp[j], dp[j - a[i]['c']] + a[i]['w'])
    print(max(dp))

t = 1
for _ in range(t):
    solve()