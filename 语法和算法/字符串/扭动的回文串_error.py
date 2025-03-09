import os
import sys

n = int(input())

A = input()
B = input()

def expend(s, l , r):
    # 暴力求解回文
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return ((r - 1) - (l + 1)) >> 1

def loPa(s):
    s = '#' + '#'.join(list(s)) + '#'
    dp = [0] * len(s)
    center, right = 0, 0

    for i in range(1, len(s)):
        if i > right:
            dp[i] = expend(s, i, i)
        else:
            i_sym = 2 * center - i
            min_len = min(dp[i], right - 1)
            dp[i] = expend(s, i - min_len, i + min_len)
        if i + dp[i] > right:
            center = i
            right = dp[i] + i
    return max(dp)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = A[i:j + 1] + B[j:k + 1]
            # 用马拉车去判断最长的回文串
            ans = max(ans, loPa(s))
print(ans)      