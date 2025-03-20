#! == 新 ==

import os
import sys
input = sys.stdin.readline

# 回溯 + 剪枝 => 七步走

# 1. 确定状态 
'''
col, row, vis, path => 作为全局变量, 用于追踪当前是否合法
dfs(x, y) => 当前的位置(基础状态)
'''

# 2. 非法状态
'''
1. 下一个要去的位置超出了边界
2. 下一个要去的位置 col[xx] == 0 | row[yy] == 0
'''

# 3. 更新状态
'''
1. 标记走过 => vis[x][y] = 1
2. col[x] -= 1 && row[y] -= 1
3. 记录当前路径
'''

# 4. 结束状态
'''
1. x == n - 1 and y == n - 1 and sum(row) == 0 and sum(col) == 0
'''

# 5. 状态转移
'''
向所有合法位置扩展
'''

# 6. 还原状态
'''
1. 标记没走过 => vis[x][y] = 0
2. col[x] += 1 && row[y] += 1
3. 当前路径 pop()
'''

# 7. !状态剪枝!
'''
如果当前位置的col为0了，也就是说不能再次来到这一列了，但是左边还有剩余的没去，
那么如果去了左边就再也回不来，不去也不符合题目要求，所以就是不可能的。
col[y] == 0 and sum(col[:y]) != 0: return
row[x] == 0 and sum(row[:x]) != 0: return 
'''

def dfs(x, y):
    if row[x] == 0 or col[y] == 0: return False # 当前行或者列已经不能有格子了,就是有一个方向去不了了
    # 剪枝
    if col[y] == 0 and sum(col[:y]) != 0:
        return False
    if row[x] == 0 and sum(row[:x]) != 0:
        return False
    

    # 记录状态, 在记录状态之前一定要把所有非法的情况都剪掉！！！
    path.append(x * n + y)
    vis[x][y] = 1
    col[y] -= 1
    row[x] -= 1

    # 判断结束
    if x == n - 1 and y == n - 1 and sum(col) == 0 and sum(row) == 0:
        return True

    # 扩展
    for dx, dy in dirs:
        xx, yy  = x + dx, y + dy
        if 0 <= xx < n and 0 <= yy < n:
            if vis[xx][yy] == 0:
                if dfs(xx, yy): return True
    
    # 回溯
    path.pop()
    vis[x][y] = 0
    col[y] += 1
    row[x] += 1
    return False



n = int(input())
col = list(map(int, input().split()))
row = list(map(int, input().split()))
mp = []
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
vis = [[0] * n for i in range(n)]
path = []
dfs(0, 0) # 出发
print(*path)

# '''
# 走一步，西北的箭牌就少一个，符合情况的就是全部和为0
# '''
# def dfs(x, y):
#     # 每次进来先打标记
#     vis[x][y] = True
#     north[y] -= 1
#     west[x] -= 1
    

#     # 当前位置的箭靶数
#     path.append(A[x - 1][y - 1])
#     # 出口
#     if x == n + 1 and y == n + 1:
#         # 判断到右下角的这一条路是不是符合题目的要求的
#         # 因为有很多种可能能到左下角，但是只有一种也就是把所有的靶子数用完的这一种情况
#         if sum(north) == 0 and sum(west) == 0:
            
#             return
        
            

#     # 每层循环的操作
#     # 
#     for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         xx, yy = x + delta_x, y + delta_y
#         # 不满足的情况
#         if vis[xx][yy] or north[yy] >= 0 or west[xx] >= 0:
#             continue
#         # 满足了    
        
#         dfs(xx, yy) 
    

# n = int(input())
# # n * n, 多两行，防止越界 
# # 1 ~ n + 1 是有效位置
# A = [[row * n + col for col in range(n)] for row in range(n)]
# # 标记走没走过
# vis = [[ False for _ in range(n + 3)] for _ in range(n + 3)]
# # 1 ~ n + 1 是有效位置
# for i in range(n + 3):
#     vis[0][i] = True
#     vis[n + 2][i] = True
#     vis[i][0] = True
#     vis[i][-1] = True
# print(vis)
# path = []
# north = [0] + list(map(int, input().split())) + [0]
# west = [0] + list(map(int, input().split())) + [0]
# dfs(1, 1)
# print(path)


# import os
# import sys
# import copy
# sys.setrecursionlimit(1500000)
# # 请在此输入您的代码
# #回溯DFS+path拔旗。方格表示法为——0,0=1 0,1=1 3,3=15,行数*4+列数好像是。
# # 2，1=9
# n=int(input())
# #遍历并不是永无止境的。他需要满了则回溯，拔后则加回。
# #起
# vis=[[0]*n for _ in range(n)]
# lie=list(map(int,input().split()))
# hang=list(map(int,input().split()))
# tar=(sum(hang)+sum(lie))//2 #目标步数
# p=""
# def dfs(x,y,path,bu):
#   global p
#   vis[x][y]=1
#   hang[x]-=1
#   lie[y]-=1
#   if hang[x]==0:
#     for i in range(x):
#       if hang[i]>0:
#         return
#   if lie[y]==0:
#     for i in range(y):
#       if lie[i]>0:
#         return
#   if x==n-1 and y==n-1:
#     if sum(hang)==0 and sum(lie)==0 and bu==tar:
#       p=path
#       return#符合条件啊啊啊啊啊
#     else:
#       return#确实走到终点了，但是此路线没有符合条件。
#   for xq,yq in [(0,1),(1,0),(-1,0),(0,-1)]:
#     xi,yi=x+xq,y+yq
#     if 0<=xi<n and 0<=yi<n and vis[xi][yi]!=1 and hang[xi]>0 and lie[yi]>0:
#       dfs(xi,yi,path+"/"+str(xi*n+yi),bu+1)
#       vis[xi][yi]=0#回溯，
#       hang[xi]+=1
#       lie[yi]+=1
# dfs(0,0,"0",1)
# for i in p.split("/"):
#     print(i,end=" ")
