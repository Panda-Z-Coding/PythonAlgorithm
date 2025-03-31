import os
import sys
from queue import PriorityQueue
input = sys.stdin.readline
# d[x][y] -> 从起点到(x, y)最少花费
# 我们到达出口所用的花费不能大于E, 就可以出去
# 是水果就加上花费, 是. 就0花费

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
g = [input() for i in range(n)]
E = int(input())
inf = float('inf')

def get(x):
    if x == '.': return 0
    else: return ord(x) - ord('A') + 1 # 算出花费

def dijk(x1, y1):
    d = [[inf] * m for i in range(n)]
    d[x1][y1] = 0
    vis = set()
    q = PriorityQueue()
    q.put((d[x1][y1], x1, y1))
    while not q.empty():
        # 取出
        _, x, y = q.get()
        # 进行终点判断
        if x == x2 and y == y2:
            return d[x2][y2]
        # 判断是否已经出队列过
        if (x, y) in vis: continue
        # 没有出列过
        vis.add((x, y))
        # 扩展
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            xx, yy = x + dx, y + dy
            # 判断越界、障碍物、花费是否更小
            if 0 <= xx < n and 0 <= yy < m and (xx, yy) not in vis and g[xx][yy] != '#':
                cur = d[x][y] + get(g[xx][yy])
                if cur < d[xx][yy]:
                    # update
                    d[xx][yy] = cur
                    q.put((d[xx][yy], xx, yy))
    return inf

if E >= dijk(x1, y1):
    print("Yes")
else:
    print("No")