# 1.建立二叉树
# 2.dfs搜索所有节点

from functools import lru_cache

n = int(input())
lins = [[0]] # 下标从1开始
L = [0] + list(map(int, input().split()))
res = 0
for i in range(n):
    rr, ll = map(int, input().split())
    lins.append([rr, ll])
@lru_cache(maxsize = None)
def dfs(i, zhi):
    global res
    
    if zhi == 0:
        res += L[i]
    if lins[i][0] == -1 and lins[i][1] == -1:
        return
    else:
        if lins[i][0] != -1:
            dfs(lins[i][0], zhi + 1)
        if lins[i][1] != -1:
            dfs(lins[i][1], zhi - 1)
            
dfs(1, 0)
print(res)