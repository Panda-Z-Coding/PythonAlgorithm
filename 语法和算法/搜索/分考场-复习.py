# a, b 认识, 这种感觉就像图一样, 所以我们要建立邻接表
# 这是一个回溯 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import defaultdict
# 最少分几个考场 -> 搜索遍历一遍

# dfs(x, cnt) => 当前处理x, 当前所有的房间数量


n = int(input())
m = int(input())

# 用邻接矩阵吧
gp = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    gp[a][b] = 1
    gp[b][a] = 1
rooms = [[0] * (n + 1) for i in range(n + 1)]
ans = float('inf') # 设置为n, 表示每个人都要开一个房间 
def dfs(x, cnt): 
    global ans
    # x => 当前处理第x个人
    # cnt => 当前所有的房间数
    # 剪枝
    if cnt >= ans:
        return
    # 结束
    if x > n:
        # 处理到最后一个人
        # 不能 x == n 因为这样就处理不到最后一个人
        ans = min(ans, cnt)
        return
    
    # 判断当前节点能去哪个房间
    # 先遍历当前的所有房间, 分配位置, 向下递归
    for i in range(1, cnt + 1):
        k = 0 # 用于追踪x要被分配到房间的哪一个位置
        # 遍历这个房间, 有两种情况
        # 1. 房间空, 直接放
        # 2. 房间里面有人, 一个一个遍历看是否是和x有关系的人, 并且更新指针k
        while rooms[i][k] != 0 and gp[x][rooms[i][k]] == 0:
            k += 1
        # 如果当前位置是空
        if rooms[i][k] == 0:
            # 放置
            rooms[i][k] = x
            # 向下一层
            dfs(x + 1, cnt) # 放到已经开的房间了, cnt 不变
            rooms[i][k] = 0 # 回溯, 当前放发不一定是最优的, 要考虑所有的情况
            break # 当前x放置完了 
    # 如果可以运行到这里, 说明x不能放在已经有的房间里面, 需要重新开一个房间
    rooms[cnt + 1][0] = x
    # 递归
    dfs(x + 1, cnt + 1)
    rooms[cnt + 1][0] = 0

dfs(1, 0)
print(ans)