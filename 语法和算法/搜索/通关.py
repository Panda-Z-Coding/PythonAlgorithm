import os
import sys

from queue import PriorityQueue
from collections import defaultdict

# 如果我当前弹出来的最小的关卡都没办法, 那么游戏结束

g = defaultdict(list) # 
q = PriorityQueue()
n, p = map(int, input().split())
ge = [0] * (n + 1) # 完成之后获得的经验
for i in range(1, n + 1):
    f, s, k = map(int, input().split())
    g[f].append((i, k)) # 前置关卡、完成之后获取的经验、需要的经验
    ge[i] = s
# print(get)
# vis = [False] * (n + 1)
# bfs+优先队列
# print(g)
if p < g[0][0][0]:
    print(0)
else:
    ans = 0
    q.put((g[0][0][1], 1)) # 从1开始出发
    while not q.empty():
        w, u = q.get()
        # print(f"p = {p}")
        # print(w, u)
        
        # if vis[u]: continue
        if p < w: break # 最小的都挑战不了了
        ans += 1
        # vis[u] = True
        p += ge[u]
        for v, w in g[u]:
            q.put((w, v))
                
    print(ans)             
