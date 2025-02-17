import sys
import math
import collections
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
   n, k, c = map(int, input().split())
   depth = [0] * (n + 1)
   max_dep1 = [0] * (n + 1)
   max_dep2 = [0] * (n + 1)
   g = [[] for _ in range(n + 1)]
   for _ in range(n - 1):
       a, b = map(int, input().split())
       g[a].append(b)
       g[b].append(a)
   def dfs(dep, u, pa):
        for v in g[u]:
            if v != pa:
                dep[v] = dep[u] + 1
                dfs(dep, v, u)
   r1, r2 = 0, 0
   depth[1] = 0
   dfs(depth, 1, -1)
   for i in range(1, n + 1):
       if depth[i] > depth[r1]:
           r1 = i
   max_dep1[r1] = 0
   dfs(max_dep1, r1, -1)
   for i in range(1, n + 1):
       if max_dep1[i] > max_dep1[r2]:
           r2 = i
   max_dep2[r2] = 0
   dfs(max_dep2, r2, -1)
   if c >= k:
       # 如果挪一步的代价大于走一步的收获，那就不挪了
       print(max(depth) * k)
       return
   ans = 0
   # 把所有节点作为根节点取最⼤值
   for i in range(1, n + 1):
       ans = max(ans, max(max_dep1[i], max_dep2[i]) * k - depth[i] * c)
   print(ans)

t = 1
t = ii()
for _ in range(t):
    solve()