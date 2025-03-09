# 同时遍历两个树，如果权值对不上，那就直接结束递归（剪枝）
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())

F_val = [0] + list(input().split()) # 下标从1开始，与下边比较的时候相同
S_val = [0] + list(input().split())

F_t = defaultdict(list)
S_t = defaultdict(list)

for i in range(n-1):
    u, v = map(int, input().split())
    F_t[u].append(v)
    

for i in range(m-1):
    u, v = map(int, input().split())
    S_t[u].append(v)

ans = 0
# 同步dfs
def dfs(x, y, step):
    # x, y => 表示当前遍历第一颗树第x编号的，y同理
    #? step 表示当前的公共前缀长度
    global ans
    #! 如果当前的权值对不上，直接return
    if F_val[x] != S_val[y]:
        return
    #! 存解
    ans = max(ans, step + 1)
    
    # 对上了，按照层遍历
    for i in F_t[x]: # ! 不是字典的长度，是子节点数组的长度!!!
        for j in S_t[y]:
            dfs(i, j, step + 1)
dfs(1, 1, 0)
print(ans)