
#? 这就是一个邻家打劫问题
# dp[i] = max(dp[i-1], dp[i-2] + value) # 取和不取

import os
import sys

input  = sys.stdin.readline

s = input()

a_a = ord('a') - 1

dp = [0] * len(s)
dp[0] = ord(s[0]) - a_a

if len(s) == 1:
    print(dp[-1])
    exit(0)

dp[1] = max(ord(s[0]) - a_a, ord(s[1]) - a_a)
for i in range(2, len(s)):
    dp[i] = max(dp[i-1], dp[i-2] + ord(s[i]) - a_a)
# print(a_a)
print(dp[-1])

