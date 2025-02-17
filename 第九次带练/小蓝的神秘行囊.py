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
    n, V, M = il()
    f = [[0] * (M + 1) for _ in range(V + 1)]
    for _ in range(n):
        v, m, w = il()
        for j in range(V, v - 1,-1):
            for k in range(M, m - 1, -1):
                f[j][k] = max(f[j][k], f[j - v][k - m] + w)
    print(f[V][M])

t = 1
for _ in range(t):
    solve()