import os
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
g = defaultdict(list)

for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(u, fa):
    # 预处理每一个节点的深度和p[u][i]
    deep[u] = deep[fa] + 1
    p[u][0] = fa # 往上走一步
    for i in range(1, 21):
        p[u][i] = p[p[u][i - 1]][i - 1]
    for v in g[u]:
        if v == fa: continue
        dfs(v, u)

def LCA(x, y):
    # 求x, y的最近公共祖先
    # 先假设x更深
    if deep[x] < deep[y]:
        x, y = y, x # 交换
    # 然后x开始往上跳
    # 从大枚举到小, 如果走2^i步使得deep[x] < deep[y] 不能走
    for i in range(20, -1, -1):
        if deep[p[x][i]] >= deep[y]:
            x = p[x][i]
    
    if x == y:
        # 如果这时候两个相同直接返回
        return x
    
    # 如果x!=y => 这时候deep[x] == deep[y], 一起往上走
    # 走到第一个非祖先的点, 防止再往上走都是公共祖先
    for i in range(20, -1, -1):
        if p[x][i] != p[y][i]:
            x = p[x][i]
            y = p[y][i]
    
    return p[x][0] # 往上再走一步就是最近的公共祖先



deep = [0] * (n + 1) # 每一个节点的深度
p = [[0] * 22 for i in range(n + 1)]
# 通过dfs预处理每一个节点的信息
dfs(1, 0) # 根节点的父节点是0, 才能+1是1
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    print(LCA(a, b))


