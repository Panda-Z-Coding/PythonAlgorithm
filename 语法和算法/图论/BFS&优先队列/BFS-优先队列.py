# 染色时间
import os
import sys
input = sys.stdin.readline
from queue import PriorityQueue
# BFS-优先队列 => 处理带权图的最短路径问题
inf = float('inf')
# 先输入
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)] # 染色时间
# print(a)
# x, y 位置的最小染色时间
dis = [[inf] * m for i in range(n)]
# 边界
dis[0][0] = a[0][0]
# 标记数组 - x, y 是否出过队列
vis = [[False] * m for i in range(n)]
# 1. 优先队列
q = PriorityQueue()
# 2. 把起点放入优先队列中, 优先级为第一个元素, 越小越优先
q.put((dis[0][0], 0, 0)) # 从左上角出发
ans = 0
while not q.empty():
    # 队列不为空
    # 1. 取出最优的元素
    d, x, y = q.get()
    # 2. 判断x,y 是否已经出过队列
    if vis[x][y]: continue
    # 3. 如果没有出过则可以更新vis和ans
    vis[x][y] = True
    ans = max(ans, dis[x][y])
    # 4. 向四周扩展节点
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        xx, yy = x + dx, y + dy
        # 判断是否越界 & 是否vis
        if 0 <= xx < n and 0 <= yy < m and not vis[xx][yy]:
            # 判断距离是否会更小
            if d + a[xx][yy] < dis[xx][yy]: # 如果从x,y染色到xx, yy 的时间比当前记录都还少就更新
                dis[xx][yy] = d + a[xx][yy]
                # 入队
                q.put((dis[xx][yy], xx, yy))

print(ans)