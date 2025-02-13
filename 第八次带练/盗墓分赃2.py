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
   n = int(input())
   a = [0] * (n + 1)
   sum = 0
   for i in range(1, n + 1):
       a[i] = int(input())
       sum += a[i]
   if sum % 2 != 0 or n % 2 != 0:
       print("no")
       return
   sum = sum // 2  # 背包体积
   dp = [0] * (sum + 1)
   for i in range(1, n + 1):
       for j in range(sum, a[i] - 1, -1):
           dp[j] = max(dp[j], dp[j - a[i]] + a[i])
   if dp[sum] == sum:
       print("yes")
   else:
       print("no")

t = 1
for _ in range(t):
    solve()