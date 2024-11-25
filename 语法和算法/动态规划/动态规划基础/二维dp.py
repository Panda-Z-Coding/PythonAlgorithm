import os
import sys

# 请在此输入您的代码
N = int(input())
a = [[0] * (N + 1)]
dp = [[0] * (N + 1) for i in range(N + 1)]
for i in range(N):
    a.append([0] + list(map(int, input().split())))

# dp[i][j] 表示从(i, j) 出发到底部的最大和

# 终点 dp[1][1]
# (i, j)可以走到(i + 1, j)和(i + 1,j + 1)
# dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + a[i][j]

for i in range(N, 0, -1):
    for j in range(1, i + 1):
        if i == N:
            dp[i][j] = a[i][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + a[i][j]

print(dp[1][1])

