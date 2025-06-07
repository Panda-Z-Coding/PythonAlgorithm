import os
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maxn = 3 * 10 ** 6
dp = [0] * maxn

for i in range(n):
    l, r = map(int, input().split())
    dp[l + r] += 1 # 记录中点的个数

# 做前缀和
for i in range(1, maxn):
    # 直接在dp基础上前缀和
    dp[i] += dp[i-1]

for i in range(m):
    cnt = 0
    L, R = map(int, input().split())
    cnt += dp[2*R] - dp[2*L - 1]

    print(cnt)


