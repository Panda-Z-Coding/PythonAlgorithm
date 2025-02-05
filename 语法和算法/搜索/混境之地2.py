# 只能使用一次破墙
# 通过染色法来搜寻能否达到
# 起点出发染1色，终点出发染2色，便利所有的墙看上下左右能否构成联通
from sys import exit
import sys
sys.setrecursionlimit(100000)
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())

A, B, C, D = map(int, input().split())
A, B, C, D = A - 1, B - 1, C - 1, D - 1

mp = [list(input()) for i in range(n)]
# print(mp)
vis = [[0] * m for i in range(n)]  # 用于存储访问过这个是属于哪一个色块

def dfs(x, y, v):
    # x, t 表示当前节点的位置
    # v 标记色块
    vis[x][y] = v
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and mp[nx][ny] == '.':
            dfs(nx, ny, v) # 向能到达的所有地方染色

se1 = False
se2 = False

dfs(A, B, 1) # 先从起点开始染1色
if vis[C][D] == 1:
    # 如果不用破墙直接能去到终点
    print("Yes")
else:
    # 遍历所有的墙，看能不能联通
    # 先从终点染2色
    dfs(C, D, 2)
    for i in range(n):
        for j in range(m):
            if mp[i][j] == '#':
                # 向四周检查
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        # 如果四周能连接到se1
                        if vis[nx][ny] == 1:
                            se1 = True
                        if vis[nx][ny] == 2:
                            se2 = True
                if se1 and se2:
                    # 在这个墙四周的联通是否后
                    print("Yes")
                    sys.exit()
                # 还原
                se1 = False
                se2 = False

    print("No")
 
