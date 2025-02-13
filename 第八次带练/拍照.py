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
    ans = 0
    l, r = [1 for _ in range(n)], [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if a[j] <= a[i]:
                l[i] = max(l[i], l[j]+1)
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if a[j] <= a[i]:
                r[i] = max(r[i], r[j]+1)
    for i in range(n):
        ans = max(ans, l[i]+r[i]-1)
    print(n-ans)

t = 1
for _ in range(t):
    solve()