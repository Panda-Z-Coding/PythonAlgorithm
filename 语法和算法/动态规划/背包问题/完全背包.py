'''
有无数个物品
'''

#! dp[i][j] 前i种物品，体积为j的最大值
# 不拿: dp[i][j] = dp[i-1][j]
# 拿: dp[i][j] = max(dp[i-1][j-wi] + vi, dp[i-1][j-2wi] + 2vi,...,dp[i-1][j-kwi] + kvi)

# 三中循环

# 优化
# dp[i][j] = max(dp[i-1][j], dp[i][j-w] + v)

#? 01: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

#? 完全: dp[i][j] = max(dp[i-1][j], dp[i][j-w] + v)

N, V = map(int, input().split())
# dp = [[0] * (V + 1) for i in range(N + 1)]

'''
for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(0, V + 1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j - w] + v)
print(dp[N][V])
'''
# 一维数组更新
dp = [0] * (V + 1)
for _ in range(N):
    w, v = map(int, input().split())
    #? 后面的是要基于前面的推出来的, 所以从前面往后更新
    # 要是01背包的话, for i in range(V + 1, w, -1)
    for j in range(w, V + 1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[V])