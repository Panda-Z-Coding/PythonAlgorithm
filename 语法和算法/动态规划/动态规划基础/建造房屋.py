import os
import sys

# 请在此输入您的代码
# dp[i][j] => 前i条街，成本为j的方案数 =》 dp[N][K]
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][j-M]
# 只有街的数量和成本才能定死状态！

N, M, K = map(int, input().split())
MOD = int(1e9 + 7)
dp = [[0] * (K + 1) for i in range(N + 1)]

for i in range(K + 1):
    dp[0][i] = 1
# 枚举街数
for i in range(1, N + 1):
    # 枚举成本
    for j in range(1, K + 1):
        # 枚举能建造房子的个数
        for m in range(1, M + 1):
            if j >= m:
                # 不能欠债
                dp[i][j] += dp[i-1][j-m]
                dp[i][j] %= MOD
print(dp)
print(dp[N][K])