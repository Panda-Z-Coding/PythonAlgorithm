import os
import sys

# 请在此输入您的代码

# 1 2 3 4 5

n = int(input())
m = int(input())
# 关系邻接表
nums = [[0]*(n+1) for i in range(n+1)]

# 考场表
rooms = [[0]*(n+1) for i in range(n+1)]

ans = float('inf')

# 构造邻接表
for i in range(m):
    a, b = map(int, input().split())
    nums[a][b] = 1
    nums[b][a] = 1


def dfs(x, cnt):
    '''
    x:   表示当前是第x个人
    cnt: 表示当前开了几个房间了
    '''
    global ans

    if cnt >= ans:
        return
    # 出口
    if x > n:
        ans = min(ans, cnt)
        return
    
    for i in range(1, cnt + 1):
        k = 0
        # 若房间的第k个位置没有人并且这个房间
        while rooms[i][k] != 0 and nums[x][rooms[i][k]] == 0:
            k += 1
        if rooms[i][k] == 0:
            rooms[i][k] = x
            # 不用新开一个
            dfs(x + 1, cnt)
            rooms[i][k] = 0
            break
    # 上面都没找到，新开一个
    rooms[cnt + 1][0] = x
    dfs(x + 1, cnt + 1)
    rooms[cnt + 1][0] = 0
dfs(1, 0)
print(ans)