# from collections import deque

# def bfs(begin, end):
#     # 将字符串转换为列表
#     begin = list(begin)
#     end = list(end)
    
#     q = deque()
#     q.append([begin.index('.'), begin, 0])
#     vis = set()
#     vis.add(tuple(begin))  # 使用元组作为哈希表的键，列表是不可哈希的!
    
#     dirs = {
#         0: [1, 3],
#         1: [0, 2, 4],
#         2: [1, 5],
#         3: [0, 4, 6],
#         4: [1, 3, 5, 7],
#         5: [2, 4, 8],
#         6: [3, 7],
#         7: [4, 6, 8],
#         8: [5, 7]
#     }

#     while q:
#         pos, cur, step = q.popleft()
#         if cur == end:
#             return step
#         for next_pos in dirs[pos]:
#             next_cur = cur[:]  # 复制当前状态
#             next_cur[pos], next_cur[next_pos] = next_cur[next_pos], next_cur[pos]  # 交换元素
#             if tuple(next_cur) not in vis:
#                 vis.add(tuple(next_cur))
#                 q.append([next_pos, next_cur, step + 1])
#     return -1

# # 输入
# begin_str = input().strip()
# end_str = input().strip()

# # 检查初始状态和目标状态是否相同
# if begin_str == end_str:
#     print(0)
# else:
#     ans = bfs(begin_str, end_str)
#     print(ans)

import os
import sys

# 第一个问题？如何确定bfs的状态？
'''
- 这里只能用图来表示当前的状态，因为我们要考虑所有的数字放在哪个地方

- 如何表达换位，在一维中
    - 12345678.
    - 先判断这个空格在第几号位置，每个位置能满足交换的位置写到字典中

dirs = {1: [4, 2], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9]
7: [4, 8], 8: [5, 7, 9], 9: [8, 6]
}

'''
from collections import deque
# 每一个位置（.）能够交换的位置
dirs = {
    1: [4, 2], 
    2: [1, 3, 5], 
    3: [2, 6], 
    4: [1, 5, 7], 
    5: [2, 4, 6, 8], 
    6: [3, 5, 9],
    7: [4, 8], 
    8: [5, 7, 9], 
    9: [8, 6]
}

def bfs():
    q = deque()
    q.append([be_pos, begin, 0]) #当前. 的位置, 当前局面, 当前的步数
    vis.add(tuple(begin))
    while q:
        pos, cur ,step = q.popleft()
        # 判断是否找到
        if cur == end:
            print(step)
            return True
        
        # 扩展节点
        for next_pos in dirs[pos]:
            # 计算当前的局面
            next_cur = cur[:]
            next_cur[pos], next_cur[next_pos] = next_cur[next_pos], next_cur[pos]
            # 交换之后
            if tuple(next_cur) not in vis:
                vis.add(tuple(next_cur))
                q.append([next_pos, next_cur, step + 1])


    return False
        
# 输入
begin = [' '] + list(input()) # 下标从1开始
be_pos = begin.index('.') 
end = [' '] + list(input())
end_pos = end.index('.')
vis = set()
# print(be_pos, end_pos)
ans = 0
if not bfs():
    print(-1)