import os
import sys

# 直接bfs，状态节点再加一个字符串就行了

from collections import deque

data = [input() for i in range(30)]
flag = [[0] * 50 for i in range(30)]
q = deque()
q.append([0, 0, ""])
while q: 
    x, y, st = q.popleft()

    if  x < 0 or y < 0 or x >= 30 or y >= 50 or data[x][y] == "1" or flag[x][y]:
        flag[x][y] = 1  # 标记走过
        q.append((x + 1, y, st + "D"))  # 按照最小字典序先向下
        q.append((x, y - 1, st + "L"))  # 向左
        q.append((x, y + 1, st + "R"))  # 向右
        q.append((x - 1, y, st + "U"))  # 向上
    if x == 29 and y == 49:
        print(st)
        break 

# import os
# import sys

# # 请在此输入您的代码

# data = [input() for i in range(30)]  # data为字符数组，30行50列，数组太大这里列不下所以以空数组代替

# flag = [[0] * 50 for _ in range(30)]  # 标记数组

# def  matchCondition(x, y):  # 判断是否符合条件
#     if x < 0 or y < 0 or x >= 30 or y >= 50 or data[x][y] == "1" or flag[x][y]:
#         return False
#     return True


# def step(i, j):
#     q = [(i, j, "")]  # 无法使用队列queue，用列表凑合，会慢很多
#     while q:  # 队列不为空这循环
#         x, y, strs = q.pop(0)  # 弹出队列头元素
#         if matchCondition(x, y):
#             flag[x][y] = 1  # 标记走过
#             q.append((x + 1, y, strs + "D"))  # 按照最小字典序先向下
#             q.append((x, y - 1, strs + "L"))  # 向左
#             q.append((x, y + 1, strs + "R"))  # 向右
#             q.append((x - 1, y, strs + "U"))  # 向上
#         if x == 29 and y == 49:  # 到达终点返回答案
#             return strs

# ans = step(0, 0)
# print(ans)
