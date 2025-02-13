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
    a = [0] + il()
    b = [0] + il()
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = max(f[i-1][j], f[i][j-1])
            if a[i] == b[j]:
                f[i][j] = max(f[i][j], f[i-1][j-1] + 1)
    print(f[n][m])

t = 1
for _ in range(t):
    solve()