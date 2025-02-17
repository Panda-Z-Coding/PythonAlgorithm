# 每个士兵可以训练多次 -> 完全背包

n, m, k = map(int, input().split())
# 士兵人数、 计划数、 精力数
a = list(map(int, input().split())) # 士兵的初始值
b = list(map(int, input().split())) # 每种训练的提升值
c = list(map(int, input().split())) # 每种训练消耗的精力

# dp[p][j] 表示精力为j的时候运用计划p训练的最大下限
# dp[p][j] = max(dp[p][j], dp[p][j-c[i]] + b[i])
# k >= j >= bi

