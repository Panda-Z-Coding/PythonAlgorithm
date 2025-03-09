import os
import sys

# dfs

# 建立棋盘
# mp = [[0] * 5] * 5 不行
mp = [[0] * 5 for i in range(5)]
ans = 0

def check():
    global ans
    a = 0
    for i in range(5):
        for j in range(5):
            if mp[i][j] == 1:
                a += 1
    if a != 13:
        return
    
    count = 0
    count += mp[0][0] +  mp[1][1] + mp[2][2] + mp[3][3] + mp[4][4]
    if count % 5 == 0:
        return
    count = 0
    count += mp[0][4] +  mp[1][3] + mp[2][2] + mp[3][1] + mp[4][0]
    if count % 5 == 0:
        return
    
    for i in range(5):
        count = 0
        count += mp[i][0] + mp[i][1] + mp[i][2] + mp[i][3] + mp[i][4]
        if count % 5 == 0:
            return
        
        count = 0
        count += mp[0][i] + mp[1][i] + mp[2][i] + mp[3][i] + mp[4][i]
        if count % 5 == 0:
            return
    
    ans += 1
    




def dfs(num):
    # num: 当前枚举到多少个棋子，一个一个棋子横着来
    if num == 25:
        check()
        return

    x, y = num // 5, num % 5 # 下标从0开始的
    mp[x][y] = 1 # 先放白棋
    dfs(num + 1)
    mp[x][y] = 0
    dfs(num + 1)

dfs(0)
print(ans)
