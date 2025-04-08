import os
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import defaultdict
# 用w[u][i] 存储从主根节点到u这个节点, i这个元素出现的次数
# 要求节点 u -> v 的某个元素出现的次数就通过 w[u][i] - w[v][i], 如果元素i和a[u]相同要再加1, 把自己加回来

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
g = defaultdict(list)
# 存储从根节点到u, i这个元素出现的个数
w = [[0] * 30 for i in range(n + 1)] # 下标从1开始
# 没有初始话w
##for i in range(n + 1):
##    for m in a:
##        w[i][m] = 1
dep = [0] * (n + 1) # 存储深度
p = [[0] * 30 for i in range(n + 1)] # u往上走2^i步的节点



def dfs(u, fa):
    # 先预处理每个节点
    # 存储每个节点的深度
    # 存储每个节点从根节点到这里元素i出现的次数
    # 存储p数组
    dep[u] = dep[fa] + 1
    p[u][0] = fa
    # 这里每个元素出现的次数可以直接转移
    for i in range(1, 21): # 遍历找每个元素
        # 如果和当前节点不相同就直接转移
        w[u][i] = w[fa][i]
    w[u][a[u]] += 1
    # 更新p数组
    for i in range(1, 22):
        p[u][i] = p[p[u][i - 1]][i - 1]
    # 扩展
    for v in g[u]:
        if v == fa: continue
        dfs(v, u)

def lca(x, y):
    # 求lca
    if dep[x] < dep[y]:
        x, y = y, x
    # dep[x] >= dep[y]
    # 深度大的向上走
    for i in range(21, -1, -1):
        # 倒序尝试
        if dep[p[x][i]] >= dep[y]:
            x = p[x][i]
    
    if x == y:
        return x
    # dep[x] == dep[y] 
    # 如果还不相同, 就一起向上走
    for i in range(20, -1, -1):
        if p[x][i] != p[y][i]:
            x = p[x][i]
            y = p[y][i]
    
    return p[x][0]
    


def solve(s, t):
    # 首先我要求出这两货的lca
    lc = lca(s, t)
    # 求出从 s->lc 和从 t->lc的树上差分
    # 我用一个数组下标来表示这个种类, 每次+, 最后输出不为0的个数
    
    ans = 0
    for i in range(1, 21):
        num = w[s][i] + w[t][i] - 2 * w[lc][i] + (a[lc] == i)
        if num > 0:
            ans += 1

    
    return ans





for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

dfs(1, 0)
# print(w)
for i in range(q):
    s, t = map(int, input().split())
    print(solve(s, t))


                                                                                                       
