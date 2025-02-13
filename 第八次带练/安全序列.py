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
    n, k = map(int, input().split(' '))
    f = [0]*(n+10)
    f[0] = 1
    for i in range(1, n + 1):
        f[i] = f[i - 1]
        if i >= k + 1:
            f[i] = (f[i] + f[i - (k + 1)])%mod
        else:
            f[i] += 1
    print(f[n])

t = 1
for _ in range(t):
    solve()