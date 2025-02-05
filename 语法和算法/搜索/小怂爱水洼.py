import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

res = 0

vis = [[False] * M for _ in range(N)]
coor = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    s = coor[x][y]  # 读取当前水塘水的数量
    vis[x][y] = True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny] and coor[nx][ny]:
            s += dfs(nx, ny)  # 从四周流向这个水洼
    
    return s

for i in range(N):
    for j in range(M):
        if coor[i][j] and not vis[i][j]:
            ans = dfs(i, j)
            res = max(ans, res)

print(res)
