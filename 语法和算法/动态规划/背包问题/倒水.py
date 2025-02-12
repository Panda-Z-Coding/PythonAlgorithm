n, m = map(int,input().split())
# 客人数量和水的体
dp = [[0] * (m + 1) for i in range(n + 1)]
## dp[i][j] 前i个客人 能消耗水量为j 的最大满意度
## dp[n][m]

for i in range(1, n + 1):
    a, b, c, d, e = map(int, input().split())
    for j in range(m + 1):
        if j < a:
            dp[i][j] = dp[i-1][j] + e
        elif a <= j < c:
            dp[i][j] = max(dp[i-1][j] + e, dp[i-1][j - a] + b)
        else:
            dp[i][j] = max(dp[i-1][j] + e, dp[i-1][j-a] + b, dp[i-1][j-c] + d)
print(dp[n][m])

# dp2[j] 表示水量为j的时候的最大满意程度
dp2 = [0] * (m + 1)
for i in range(1, n + 1):
    a, b, c, d ,e = map(int, input().split())
    for j in range(m, -1, -1):
        # 从后往前遍历所有的水量
        if j < a:
            dp2[j] = dp2[j] + e
        elif a <= j < c:
            dp2[j] = max(dp2[j] + e, dp2[j-a] + b)
        else:
            dp2[j] = max(dp2[j] + e, dp2[j-a] + b, dp2[j-c] + d)
print(dp2[m])