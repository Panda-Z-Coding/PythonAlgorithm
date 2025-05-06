import os
import sys
sys.setrecursionlimit(100000)

# 用一个地图来存当前的状态然后回溯去求解
ans = 0
# 下标从1开始

def dfs(x, i, j):
    # 当前是第x个, 放置到16就是放完了, 记录答案
    global ans

    if x == 16:
        ans += 1
        # print(*mp, sep='\n')
        return
    
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        xx, yy = i + dx, j + dy
        if 1 <= xx < 5 and 1 <= yy < 5:
            if mp[xx][yy] == 0:
                mp[xx][yy] = 1
                dfs(x + 1, xx, yy)
                mp[xx][yy] = 0  
mp = [[0] * 5 for i in range(5)] 
for i in range(1, 5):
    for j in range(1, 5):
        mp[i][j] = 1
        dfs(1, i, j)
        mp[i][j] = 0

print(ans)

