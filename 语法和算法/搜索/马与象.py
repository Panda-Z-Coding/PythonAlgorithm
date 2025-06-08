import os
import sys
input = sys.stdin.readline
from collections import deque
# from collections import deque
ma = [(-1, -2), (-2, -1), (1, 2), (2, 1), (-1, 2), (1, -2), (-2, 1), (2, -1)]
xiang = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
INF = float('inf')
# 搜索

# 任意一方先手、每一方都可以连续走任意布
# 输出最小的步数

# 用bfs求出马和象各自可能到达的地方，并且记录到这里的距离


def bfs(x, y, dis, p):
    '''
    (x, y): 起点
    dis: 记录到达位置花了多少步的棋盘
    p: 走路方式
    '''
    q = deque()
    q.append([x, y, 0])
    vis = set()
    vis.add((x, y))
    dis[x][y] = 0
    while q:
        tx, ty, cnt = q.popleft()
        for dx, dy in p:
            xx, yy = tx + dx, ty + dy
            if 0 <= xx < n+1 and 0 <= yy < n+1 and (xx, yy) not in vis:
                q.append([xx, yy, cnt + 1])
                dis[xx][yy] = cnt + 1
                vis.add((xx, yy))
    

n, x1, y1, x2, y2 = map(int, input().split())
dis1 = [[INF] * (n + 1) for i in range(n + 1)] # ma
dis2 = [[INF] * (n + 1) for i in range(n + 1)] # xaing


bfs(x1, y1, dis1, ma) # 马走过的
bfs(x2, y2, dis2, xiang) # 像走过的

# O(n^2)
ans = INF
for i in range(n + 1):
    for j in range(n + 1):
        ans = min(ans, dis1[i][j] + dis2[i][j])

if ans == INF:
    print(-1)
else:
    print(ans)


