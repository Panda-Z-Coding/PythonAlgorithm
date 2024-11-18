# import os
# import sys

# # 请在此输入您的代码

# def dfs(x, y):
#     # 每次进来先打标记
#     vis[x][y] = True
#     north_w[y] += 1
#     west_w[x] += 1
    

#     # 当前位置的箭靶数
#     path.append(A[x - 1][y - 1])
#     # 出口
#     if x == n + 1 and y == n + 1:
#         return

#     # 每层循环的操作
#     # 
#     for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         xx, yy = x + delta_x, y + delta_y
#         # 不满足的情况
#         if vis[xx][yy] or north_w[yy] >= north[yy] or west_w[xx] >= west[xx]:
#             continue
#         # 满足了    
        
#         dfs(xx, yy) 
    

# n = int(input())

# north_w = [0] * (n + 2) 
# west_w = [0] * (n + 2)
# # n * n, 多两行，防止越界 
# # 1 ~ n + 1 是有效位置
# A = [[row * n + col for col in range(n)] for row in range(n)]
# print(A)
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


import os
import sys
import copy
sys.setrecursionlimit(1500000)
# 请在此输入您的代码
#回溯DFS+path拔旗。方格表示法为——0,0=1 0,1=1 3,3=15,行数*4+列数好像是。
# 2，1=9
n=int(input())
#遍历并不是永无止境的。他需要满了则回溯，拔后则加回。
#起
vis=[[0]*n for _ in range(n)]
lie=list(map(int,input().split()))
hang=list(map(int,input().split()))
tar=(sum(hang)+sum(lie))//2 #目标步数
p=""
def dfs(x,y,path,bu):
  global p
  vis[x][y]=1
  hang[x]-=1
  lie[y]-=1
  if hang[x]==0:
    for i in range(x):
      if hang[i]>0:
        return
  if lie[y]==0:
    for i in range(y):
      if lie[i]>0:
        return
  if x==n-1 and y==n-1:
    if sum(hang)==0 and sum(lie)==0 and bu==tar:
      p=path
      return#符合条件啊啊啊啊啊
    else:
      return#确实走到终点了，但是此路线没有符合条件。
  for xq,yq in [(0,1),(1,0),(-1,0),(0,-1)]:
    xi,yi=x+xq,y+yq
    if 0<=xi<n and 0<=yi<n and vis[xi][yi]!=1 and hang[xi]>0 and lie[yi]>0:
      dfs(xi,yi,path+"/"+str(xi*n+yi),bu+1)
      vis[xi][yi]=0#回溯，
      hang[xi]+=1
      lie[yi]+=1
dfs(0,0,"0",1)
for i in p.split("/"):
    print(i,end=" ")