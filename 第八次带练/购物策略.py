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
    t = [0] * (n + 1)
    c = [0] * (n + 1)
    v = 0
    for i in range(1, n + 1):
       t[i], c[i] = il()
       t[i] += 1
       v = max(v, t[i])
    v += n
    f = [float('inf')] * (v + 1)
    f[0] = 0
    for i in range(1, n + 1):
       for j in range(v, t[i] - 1, -1):
           f[j] = min(f[j], f[j - t[i]] + c[i])
    ans = min(f[n:v+1])
    print(ans)

t = 1
for _ in range(t):
    solve()