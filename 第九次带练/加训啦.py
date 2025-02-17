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
    
N = 11000
M = N * 2
mod = 1000000007
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = []

def solve():
    n, m, k = il()
    inf = float('inf')
    a = [0] + il()
    b = [0] + il()
    c = [0] + il()
    f = [inf] * N
    f[0] = 0
    for i in range(1, m+1):
        for j in range(N):
            # 初始化DP值
            f[j] = min(f[j], f[max(0,j-b[i])]+c[i])
    def check(x):
        ans = 0
        for i in range(1,n + 1):
            if a[i] >= x:
                continue
            ans += f[x-a[i]]
        return ans <= k
    l, r = 1, N - 1
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)


t = 1
for _ in range(t):
    solve()