import os
import sys

# 次大值!!

from collections import defaultdict
sys.setrecursionlimit(100000)

def dfs(x, fu):
    # dfs是先去到叶子节点, 然后从下开始递归向上
    # 在这道题我们只需要求树的直径, 然后直径-1即可

    global ans
    dp[x] = 1
    for y in t[x]:
        # 遍历当前节点的所有子节点
        if y == fu:
            continue
        dfs(y, x) # 先去到叶子节点
        ans = max(ans, dp[x] + dp[y]) 
        dp[x] = max(dp[x], dp[y] + 1)

n = int(input())
t = defaultdict(list)
dp = [0] * (n + 1)
for i in range(n - 1):
    u, v = map(int, input().split())
    t[u].append(v)
    t[v].append(u) # 无向图, 两个节点都要
ans = 0
dfs(1, 0)
print(ans - 1)