import os
import sys
input = sys.stdin.readline
# 用deque来模拟
from collections import deque
# 从A开始, 双方轮流出牌
# 出牌时从自己的纸牌队列的头部拿走一张
# 拿走相同牌及其中间部分, 然后赢家继续出牌
# 我们要求出赢家的牌序, 没办法结束就-1
# 当某一方出掉手里最后一张牌，但无法从桌面上赢取牌时，游戏立即结束

# 主要是判断没办法结束的情况

A = deque(list(input().strip()))
B = deque(list(input().strip()))

# 用一个列表来存
cur = []
A_win = False
B_win = False
while True:
    # 退出情况
    if len(A) == 0:
        B_win = True
        break
    if len(B) == 0:
        A_win = True
        break

    # 模拟
    # 先取A队首加入cur
    ca = A.popleft()
    cur.append(ca)
    # 判断A是否能拿
    while cur.count(ca) > 1:
        # 如果插入元素的下标小于最后一个下标, 也就表示前面有相同的元素
        # 从后往前pop
        for i in range(len(cur) - 1, cur.index(ca) - 1, - 1):
            A.append(cur.pop())
        # 拿了之后要出一张牌
        ca = A.popleft()
        cur.append(ca)
    if len(A) == 0:
        B_win = True
        break
    if len(B) == 0:
        A_win = True
        break    

    # B
    cb = B.popleft()
    cur.append(cb)
    while cur.count(cb) > 1:
        for i in range(len(cur) - 1, cur.index(cb) - 1, -1):
            B.append(cur.pop())
        cb = B.popleft()
        cur.append(cb)
##print(A)
##print(B)
##print(A_win)
##print(B_win)
if A_win:
    print(*A, sep = '')
if B_win:
    print(*B, sep = '')









    
        


