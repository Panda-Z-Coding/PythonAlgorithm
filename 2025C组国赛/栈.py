import os
import sys
input = sys.stdin.readline
# 使用双向链表 + 哈希
"""
需要在线性表中频繁的删除添加就用双向链表Class Node
哈希表存储 val -> Node() 可以快速的查找是否存在相同的值
"""

# 定义一个class Node
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None    

n = int(input())
# 创建链表前哨兵和尾哨兵
head = Node(-1)
tail = Node(-1)
# 让它们连接起来
head.next = tail
tail.prev = head

# 等一下就往他们中间塞
pos = {} # 哈希表映射 val -> Node
res = 0 # 存储当前的相邻和为奇数的个数，因为是栈，添加和删除只会改变局部的，所以我们可以存取整体的
# 之后根据添加和删除的位置来计算变化值

output = [] # 每次的答案

for _ in range(n):
    num = int(input())

    # 看看存不存在
    if num in pos:
        # 如果存在
        # 先获取节点
        node = pos[num]

        # 计算变化值
        prev_node = node.prev
        next_node = node.next

        # 和前一个节点是不是和为奇数
        if prev_node != head and (prev_node.val + node.val) % 2 == 1:
            res -= 1
            # 如果是，那么要被删除，res-=1
        if next_node != tail and (next_node.val + node.val) % 2 == 1:
            res -= 1
        
        # 删除了节点之后，前后节点也可能会形成新的配对
        if (prev_node.val + next_node.val) % 2 == 1 and prev_node != head and next_node != tail:
            res += 1
            
        # 在双向链表中删除
        prev_node.next = next_node
        next_node.prev = prev_node
        del pos[num] # 直接删除Node对象

        
    
    # 往末尾添加元素
    # 先new一个对象
    new_node = Node(num)
    # 要往末尾添加元素，先获取末尾的Node
    last = tail.prev
    last.next = new_node
    new_node.prev = last
    new_node.next = tail
    tail.prev = new_node

    # 添加到哈希表
    pos[num] = new_node

    # 更新计数
    if last != head and (last.val + new_node.val) % 2 == 1:
        res += 1
    output.append(res)
print('\n'.join(map(str, output)))



