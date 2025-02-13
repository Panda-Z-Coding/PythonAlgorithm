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
    f = [0]*(m + 1)
    for _ in range(n):
        a, b, c, d, e = il()
        for i in range(m, -1, -1):
            f[i] = f[i] + e
            if i >= a:
                f[i] = max(f[i], f[i - a] + b)
            if i >= c:
                f[i] = max(f[i], f[i - c] + d)
    print(f[m])
        

t = 1
for _ in range(t):
    solve()