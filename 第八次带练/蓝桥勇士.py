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
    a = il()
    f = [0]*(n+1)
    for i in range(n):
        f[i] = 1
        for j in range(i):
            if a[j] <= a[i]:
                f[i] = max(f[i], f[j] + 1)
    print(max(f))

t = 1
for _ in range(t):
    solve()