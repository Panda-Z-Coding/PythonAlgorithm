import os
import sys
input = sys.stdin.readline
from collections import deque, defaultdict
n, m = map(int, input().split())
G = defaultdict(list)
ru = [0] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    # 计算入度
    ru[v] += 1

def topo():
    q = deque()
    for i in range(1, n + 1):
        if ru[i] == 0: q.append(i)
    while q:
        u = q.popleft()
        for v in G[u]:
            # 这里进行状态转移
            dp[v] = max(dp[v], dp[u] + 1)
            # 先减去1
            ru[v] -= 1
            if ru[v] == 0:
                q.append(v)


# dp[i] 表示从某个点走到点i的最大距离
dp = [0] * (n + 1)
topo()
print(max(dp))