import os
import sys
input = sys.stdin.readline
from itertools import accumulate

inf = float('inf')

n = int(input())
a = list(map(int, input().split()))

# 这个问题简化了, 没有收尾相连了
pres = list(accumulate(a, initial = 0))
dp = [[0] * (n + 1) for i in range(n + 1)]

for l in range(2, n + 1): # 1. 枚举区间长度 2 -> 整段
    for i in range(1, n - l + 1 + 1): # 2. 枚举左端点
        j = i + l - 1 # 3. 计算右端点
        dp[i][j] = inf #! 先假设当前区间是花费最大
        for k in range(i, j): # 枚举中断点
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + pres[j] - pres[i - 1])
print(dp[1][n])