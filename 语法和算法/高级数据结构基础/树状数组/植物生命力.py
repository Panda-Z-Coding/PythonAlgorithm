import os
import sys
from collections import defaultdict
sys.setrecursionlimit(200000)
# 有两个条件的, 可以先满足一, 另一个用线段树统计个数

def lowbit(x):
    return x & (-x)

n, s = map(int, input().split())
a = [0] + list(map(int, input().split())) # 从1开始
g = defaultdict(list)
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

d = [0] * (n + 1) # 树状数组

def add(index, x):
    while index <= n: # <= n !!!
        d[index] += x
        index += lowbit(index)

def query(index):
    ans = 0
    while index > 0:
        ans += d[index]
        index -= lowbit(index)
    return ans

##def factor(x):
##    # 求解x的所有因数
##    # 要考虑质数
##    # 
##    fac = set()
##    for i in range(1, int(x ** 0.5) + 1):
##        if x % i == 0:
##            fac.add(i)
##            fac.add(x // i)
##    return sorted(fac)
vis = [0] * (n + 1)
pd = 0
def dfs(u, fu):
    # 从下往上传递信息会出错, 要把父节点的信息传递给子节点
    global pd
    cnt = 0 # 用来数有多少个整除自己的节点
    for i in range(2 * a[u], n + 1, a[u]):
        cnt += vis[i]
    pd += query(n) - query(a[u] - 1) - cnt
    vis[a[u]] = 1
    add(a[u], 1) # 标记一下当前节点已经处理过
    for v in g[u]:
        if v != fu:
            dfs(v, u)
    # 回溯
    vis[a[u]] = 0
    add(a[u], -1) # 就是不让右边的子树失误更新左边的信息

dfs(s, -1)
print(pd)         
# print(factor(5))








