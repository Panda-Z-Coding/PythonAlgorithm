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
    m = ii()
    n = ii()
    f = [False] * (m + 1)
    f[0] = 1
    for _ in range(n):
        w = ii()
        for i in range(m,w-1,-1):
            f[i] = f[i] | f[i - w]
    ans = 0
    for i in range(m+1):
        if f[i]:
            ans = i
    print(m - ans)

t = 1
for _ in range(t):
    solve()