import sys
import math
from functools import cmp_to_key
import collections
from sys import exit
sys.setrecursionlimit(1000000)  # 设置新的递归深度限制

def read():
    return sys.stdin.readline().strip()

def ii():
    return int(read())

def il():
    return list(map(int,read().split()))
N = 200010
M = N * 2
mod = 1000000007
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = []

def solve():
    dp = [0] * N
    n, m = il()
    q = collections.deque()
    for i in range(n):
        v, w, s = il()
        for j in range(v):
            q.clear()
            num = (m-j)//v  
            for k in range(0,num+1):
                val = dp[k*v+j]-k*w
                while q and val >= q[-1][1]:
                    q.pop()
                q.append([k,val])
                if q[0][0] < k-s:  
                    q.popleft()
                dp[v*k+j] = q[0][1]+k*w
    print(dp[m])

t = 1
for _ in range(t):
    solve()