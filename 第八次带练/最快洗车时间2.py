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
    m = sum(a)
    f = [False] * (m + 1)
    f[0] = True
    # 前0台车可以使得t1 = 0
    # f[1][a[0]] = True
    for i in range(1, n + 1):
       # 第i台车
       for j in range(m, a[i-1] - 1, -1):
               f[j] |= f[j-a[i-1]]
    ans = m
    for i in range(m+1):
       if f[i]:
           ans = min(ans, max(i, m-i))
    print(ans)

t = 1
for _ in range(t):
    solve()