import sys
input = sys.stdin.readline
from collections import defaultdict
vec = defaultdict(list) # 用于存储当前节点有的子节点
g = defaultdict(list)
dp = [0] * 100100 # dp[i] -> 以i位根节点的子树最大高度

sys.setrecursionlimit(150000)

def dfs(u, fa):
    ma = 0 # 记录当前u位根的最大高度
    for v in g[u]:
        if v == fa: continue
        dfs(v, u)
        ma = max(ma, dp[v]) # 子树的信息
    dp[u] = ma + len(vec[u])
    # 因为是dfs所以是从下往上更新的
    # 从底下的子树开始最大的高度都是
    # 当前这个节点的孩子个数就是最长的子树高度

n = int(input())
for i in range(2, n + 1):
    v = int(input())
    vec[v].append(i)
    g[i].append(v)
    g[v].append(i)

dfs(1, 0)
print(dp[1])

