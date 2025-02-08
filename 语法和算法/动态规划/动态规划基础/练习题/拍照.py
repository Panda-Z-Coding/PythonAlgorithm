import os
import sys

# 请在此输入您的代码

n = int(input())

a = [0] + list(map(int, input().split()))

# 从前往后做一次LIS, dp1[i] 表示当前位置的最长上升子序列长度
# 从后往前坐一次LIS, dp2[i] 表示当前位置的最长下降的长度

dp1 = [0] + [1] * n
dp2 = [0] + [1] * n

for i in range(1, n + 1):
    for j in range(1, i):
        if a[j] <= a[i]:
            dp1[i] = max(dp1[j] + 1, dp1[i])

for i in range(n, 0, -1):
    for j in range(i + 1, n + 1):
        if a[j] <= a[i]:
            dp2[i] = max(dp2[j] + 1, dp2[i])

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dp1[i] + dp2[i] - 1)

print(n - ans)