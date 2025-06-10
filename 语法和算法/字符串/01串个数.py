import os
import sys


# 状态压缩 + 动态规划

# dp[i][mask] => 前i位最后5位符合条件的方案数

# 状态转移 => 往地位去添加0或者1

def count_ones(mask):
    return bin(mask).count('1')

def is_valid_window(mask):
    return count_ones(mask) <= 3

n = 24
window = 5

dp = [[0] * (1 << window) for i in range(n + 1)]

for mask in range(1 << window):
    if is_valid_window(mask):
        dp[window][mask] = 1

# 状态转移
for i in range(window + 1, n + 1):
    for mask in range(1 << window):
        if not is_valid_window(mask):
            continue
        for bit in [0, 1]:
            prev_mask = ((mask << 1) | bit) & ((1 << window) - 1)
            if is_valid_window(prev_mask):
                dp[i][mask] += dp[i-1][prev_mask]

res = sum(dp[n][mask] for mask in range(1 << window) if is_valid_window(mask))

print(res)




