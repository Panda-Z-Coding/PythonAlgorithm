import os
import sys
sys.setrecursionlimit(100000)
def check_all(vis):
    for s in vis:
        if 0 in s:
            return False
    return True

def check(xx, yy, next_node):
    return 0 <= xx < n and 0 <= yy < n and mp[xx][yy] == next_node and vis[xx][yy] == 0

res = []
def dfs(x, y, s):
    vis[x][y] = 1
    num = mp[x][y] # 用于判断下一步要走哪
    if x == n - 1 and y == n - 1 and check_all(vis):
        res.append(s)
        return

    next_node = num + 1
    if num == k - 1:
        next_node = 0

    for dx, dy, ns in dirs:
        xx, yy = x + dx, y + dy
        if check(xx, yy, next_node):
            if {(xx,y),(x,yy)} not in lin:
                lin.append({(x, y), (xx, yy)})
                vis[xx][yy] = 1
                dfs(xx, yy, s + ns)
                vis[xx][yy] = 0
                # 记住要还原现场lin
                lin.pop(-1)
    

dirs = [(1, 0, '4'), (0, 1, '2'), (1, 1, '3'), (-1, 0, '0'), (0, -1, '6'), (-1, 1, '1'), (-1, -1, '7'), (1, -1, '5')]

n, k = map(int, input().split())
mp = [list(map(int, input().split())) for i in range(n)]
lin = []
vis = [[0] * n for i in range(n)]

dfs(0, 0, '')
ress = sorted(res)

print(ress[0])