import os
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #! 只要涉及到dfs因为是oi赛制所有都给我设置递归深度!!!!
def dfs(u, fu):
    # 当前节点和父节点
    # 打上标记 
    dp[u] = val[u]
    for v in g[u]:
        if v != fu:
            dfs(v, u) # 向下遍历
            # 更新dp
            dp[u] += max(0, dp[v]) # 0 表示不取这个点, dp[v] 如果大于0的话就取


n = int(input())
val = [0] + list(map(int, input().split())) # 从1开始
dp = [0] * (n + 1) # dp[i] 表示从i节点出发所能达到的最大评分
g = defaultdict(list)

for i in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

dfs(1, -1)

print(max(dp))