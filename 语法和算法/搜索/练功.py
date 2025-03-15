# 按照圆形半径来判断
from math import *
from collections import deque

def dis(x1, y1, x2, y2):
    # 计算两点之间的距离
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def bfs():
    q = deque()
    q.append((1, 1))
    while q:
        x, y = q.popleft()
        if dis(n, m, x, y) <= d:
            # 出口
            return dp[x][y]
        tmp = 1e6 # 用于更新当前位置能去到的点距离终点最小的距离
        x1, y1 = 1, 1
        for i in range(x, min(x + int(d) + 1, n + 1)):
            for j in range(y, min(y + int(d) + 1, m + 1)):
                cur_to_nm = dis(n, m, i, j)
                if dis(x, y, i, j) <= d: # 能去到
                    if cur_to_nm < tmp and not dp[i][j]:
                        #? 当前枚举的位置到达终点的距离小于tmp
                        #? 没有被访问过
                        x1, y1 = i, j
                        tmp =cur_to_nm
                else:
                    break
        if not dp[x1][y1]:
            q.append((x1, y1))
            dp[x1][y1] = dp[x][y] + 1 # 走一步

n, m = map(int,input().split())
d = float(input())

dp = [[0] * (m + 1) for i in range(n + 1)]
# 用于存储当前位置的步数
dp[1][1] = 1
print(bfs())
