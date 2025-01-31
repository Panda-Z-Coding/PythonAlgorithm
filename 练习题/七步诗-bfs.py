import os
import sys
from collections import deque
n, m = map(int, input().split())
mp = []
a, b = 0, 0 # 记录🐎的位置
for i in range(n):
    row = list(input())
    mp.append(row)
    if 'S' in row:
        a, b = i, row.index('S')

# 通过deque来实现bfs搜索
def bfs(mp, a, b):
    '''a, b 是马现在所在的位置'''
    # visited = [[False for i in range(m)] for i in range(n)] # 看有没有访问过
    # 用集合存访问过的元素可以减少内存使用
    visited = set([(a, b)])
    directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)] # 🐎移动的轨迹

    queue = deque([(a, b)]) # 把🐎的位置加进来
    ans = 0 # 答案

    while queue:
        (x, y) = queue.popleft() #? 每次取队首的元素
        for dx, dy in directions: # 访问队首元素的全部相邻节点
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and mp[nx][ny] != 'x' and (nx, ny) not in visited:
                # 能到达这里就说明是合法的，合法的先插旗子，在添加进队列中
                visited.add((nx, ny))
                queue.append((nx, ny))
                if mp[nx][ny] == 'b':
                    ans += 1
    return ans


print(bfs(mp, a, b))

'''bfs 模板'''
'''
from collections import deque

def bfs(graph, start):
    # 创建一个队列用于BFS
    queue = deque([start])
    
    # 创建一个集合用于记录已访问的节点
    visited = set([start])
    
    while queue:
        # 从队列中取出一个节点
        node = queue.popleft() # 队首出
        print(node, end=" ")  # 打印当前节点
        
        if 是否到达:
            return
        
        # 遍历当前节点的所有邻居
        for neighbor in graph[node]:
            if neighbor not in visited:
                # 将未访问的邻居加入队列和已访问集合
                visited.add(neighbor)
                queue.append(neighbor)

# 示例图的邻接表表示
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 从节点 'A' 开始进行BFS
bfs(graph, 'A')
'''