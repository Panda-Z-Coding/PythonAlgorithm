import sys
sys.setrecursionlimit(100000)
from functools import lru_cache

N = int(input())
human = [list(map(int, input().split())) for i in range(N)]

D = int(input())
vis = [0] * N

@lru_cache(maxsize=None)
def dfs(n):
    # n表示当前到达哪一个人
    vis[n] = 1
    for i in range(1, N):
        if (human[i][0] - human[n][0]) ** 2 + (human[i][1] - human[n][1]) ** 2 <= D ** 2 and vis[i] == 0:
            dfs(i)

dfs(0)

for i in range(N):
    print(vis[i], end = '\n')