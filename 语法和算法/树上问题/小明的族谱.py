import os
import sys
from collections import defaultdict
# LCA => 倍增优化

# deep , p , 1 为共同祖先

n, q = map(int, input().split())
mp = defaultdict(list)
for _ in range(n-1):
    u, v = map(int ,input().split())
    mp[u].append(v)
    mp[v].append(u)

def dfs(u, fa):
    # dfs预处理每一个节点的深度和往上2^i的祖先
    deep[u] = deep[fa] + 1 # 从fa走过来
    p[u][0] = fa # 往上走一步就是fa
    for i in range(1, 21):
        p[u][i] = p[p[u][i-1]][i-1]
    # 扩展
    for v in mp[u]:
        if v != fa:
            dfs(v, u)

def lca(x, y):
    if deep[x] < deep[y]:
        # 确保x是深度比较大的那个
        x, y = y, x
    
    # 深度大的开始往上走, 直到 deep[x] < deep[y]
    for i in range(20, -1, -1):
        # 大跨步尝试
        if deep[p[x][i]] >= deep[y]:
            x = p[x][i]
    
    # 看是否相同
    if x == y:
        return x
    
    # 以前往上走, 走到要相同的前一个位置
    for i in range(20, -1, -1):
        if p[x][i] != p[y][i]:
            x = p[x][i]
            y = p[y][i]
    
    return p[x][0] # 往上一个就是


    
deep = [0] * (n + 1)
p = [[0] * 21 for i in range(n + 1)]

dfs(1, 0)


for _ in range(q):
    uu, vv = map(int, input().split())
    print(lca(uu, vv))


