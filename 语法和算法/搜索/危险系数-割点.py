import os
import sys
from collections import defaultdict
# 从站点A到站点B有ans 条路径, 而且站点C恰好被经过了ans次, C站点必然是关键点

def dfs(u, v):
    # u -> 当前节点; v -> 目标节点
    global cnt
    # 如果到达了目标节点, 路径加1, 遍历当前path的节点
    if u == v:
        cnt += 1
        for a in path:
            if a != v:
                # 目标节点不要更新
                vis_cnt[a] += 1
        return
    # 扩展节点
    for uu in g[u]:
        if vis[uu] == 0:
            vis[uu] = 1
            path.append(uu)
            dfs(uu, v)
            path.pop()
            vis[uu] = 0
    


input = sys.stdin.readline
n, m = map(int, input().split())
g = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
u, v = map(int, input().split())
# vis数组标记当前位置走过了没有
# vis_cnt数组标记当前节点走了几次
# path数组标记当前的路径, 在最后通过path数组来遍历经过的节点并且都加一
# cnt记录能到达的路径数
vis = [0] * (n + 1)
vis_cnt = [0] * (n + 1)
cnt = 0
path = []

vis[0] = vis[u] = 1

dfs(u, v)
ans = 0
# print(cnt)
# print(*vis_cnt)
for i in vis_cnt:
    if i == cnt:
        ans += 1
if not cnt:
    print(-1)
else:
    print(ans)



