import os
import sys

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] #? 这个没有(0, 0)胖子是可以不动的

#? 时间就是步数
n, k = map(int, sys.stdin.readline().split())

#? 如何定义bfs的状态
# (x, y, t) => 时间就决定了小明的宽度

mp = [[''] * n for _ in range(n)]
for i in range(n):
    row = sys.stdin.readline().strip()
    for j in range(n):
        mp[i][j] = row[j]
# 0 - n
# 0
# -
# 0 - n
from collections import deque

# five = [
#     (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
#     (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
#     (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),
#     (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
#     (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)
# ]

# three = [
#     (-1, -1), (-1, 0), (-1, 1),
#     (0, -1), (0, 0), (0, 1),
#     (1, -1), (1, 0), (1, 1)
# ]

# one = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# def check(xx, yy, t):
#     # 判断下一个要去的点是否合法， 还有当前的时间
#     if t < k:
#         # 5 * 5
#         # 要以xx, yy 为中心去判断这个区域所有的点是否合法
#         for dx, dy in five:
#             xxx, yyy = xx + dx, yy + dy
#             if not (0 <= xxx < n and 0 <= yyy < n) or mp[xxx][yyy] == '*':
#                 return False
#         return True
#     elif k <= t < 2 * k:
#         # 3 * 3
#         for dx, dy in three:
#             xxx, yyy = xx + dx, yy + dy
#             if not (0 <= xxx < n and 0 <= yyy < n) or mp[xxx][yyy] == '*':
#                 return False
#         return True
#     else:
#         # 1 * 1
#         for dx, dy in one:
#             xxx, yyy = xx + dx, yy + dy
#             if not (0 <= xxx < n and 0 <= yyy < n) or mp[xxx][yyy] == '*':
#                 return False
#         return True
def f(t): # 直接通过时间来判断宽度就行了
    if t < k:
        return 2
    elif k <= t < 2 * k:
        return 1
    else:
        return 0
    
def check(x, y, z):
    for i in range(x-z, x+z+1):
        for j in range(y-z, y+z+1):
            if mp[i][j] == '*':
                return False
    return True

vis = set()

def bfs():
    q = deque()
    q.append([2, 2, 2, 0])
    vis.add((2, 2))
    while q:
        x, y, z, t = q.popleft() # z => 当前的宽度
        # 判断当前是否到达
        if x == n - 3 and y == n - 3:
            print(t)
            break
        if z != 0:
            q.append([x, y, f(t + 1), t + 1])
        # 向四周扩展，判断的时候要带上当前的时间
        for dx, dy in dirs:
            xx, yy = x + dx, y + dy
            if  0 <= xx - z and xx + z < n and 0 <= yy - z and yy + z < n and (xx, yy) not in vis:
                if check(xx, yy, z):
                    vis.add((xx, yy))
                    q.append((xx, yy, f(t + 1) ,t + 1))
bfs()