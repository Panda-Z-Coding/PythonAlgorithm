import os
import sys
from collections import deque
# bfs
# 人肉遍历空格所在位置能和哪些地方交换, 下标从0开始
'''
ABC
012
DE 
345

'''

space = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [5, 1],
    3: [4, 0],
    4: [5, 3, 1],
    5: [2, 4]
} # 空格所在位置能交换的下标

def bfs(s):
    q = deque([(list('ABCDE*'), 5)]) # 初始状态
    while q:
        cur_s, cur_x = q.popleft()
        vis.add(tuple(cur_s))
        if cur_s == s:
            return True
        
        # 扩展
        for next_x in space[cur_x]:
            # 调换位置
            ss = cur_s[:]
            ss[cur_x], ss[next_x] = ss[next_x], ss[cur_x]
            # 加入队列
            if tuple(ss) not in vis:
                q.append((ss, next_x))
    return False



input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    s = list(input().strip())
    vis = set()
    if bfs(s):
        print(1)
    else:
        print(0)