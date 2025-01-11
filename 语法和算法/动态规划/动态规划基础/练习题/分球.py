import os
import sys

# 请在此输入您的代码

'''dp写法

dp[i][j] 表示将i个球分成j组的方案

dp[i][j] = dp[i][j-1] + (dp[i-1][j]) if i >= 1

'''
n, k = map(int, input().split())

dp = [[0] * (k + 1) for i in range(n + 1)]

# for j in range(k + 1):
#     dp[0][j] = 1 # 0个球分成多少组都是1

# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         dp[i][j] = dp[i][j-1] + dp[i-1][j]

# print(dp[n][k])

"""用组合数的地推公式"""

for i in range(n + 1):
    dp[i][0] = 1 #? C(n,0) = 1
    
for i in range(1, n + 1):
    for j in range(1, min(i + 1, k + 1)):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
print(dp[n][k] - 1)