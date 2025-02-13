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
    q = [0] * (n + 1)
    len = 0
    for i in range(n):
        l, r = 0, len
        while l < r:
            mid = (l + r + 1) // 2
            if q[mid] < a[i]:
                l = mid
            else:
                r = mid - 1
        len = max(len, r + 1)
        q[r + 1] = a[i]
    print(len)

t = 1
for _ in range(t):
    solve()