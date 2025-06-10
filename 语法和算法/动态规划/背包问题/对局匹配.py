import os
import sys


# 就是在N个中选a个人，让这a个人互相之间的差值都不等于K
maxn = 10**5 + 5
n, k = map(int, input().split())
a = list(map(int, input().split()))

# dp[i] => 积分从0->i的范围内最多多少人满足

# 首先这种关于区间长度k的, 一般可以通过对k取模来分组
# 因为积分为 x 的只会影响到 x - k 和 x + k
# 转移：
# 两种感觉：取和不取
# 1. 取 dp[i] = num[i] + dp[i-2 * k]
# 2. 不取 dp[i] = dp[i - k]

# num[i] 就是积分为i的个数，这里我们可以初始化到dp中

if k == 0:
    print(len(set(a)))
else:

    dp = [0] * maxn
    for aa in a:
        dp[aa] += 1
    
    for i in range(1, maxn):
        if i >= 2 * k:
            dp[i] = max(dp[i] + dp[i - 2 * k], dp[i - k])
        elif i >= k:
            dp[i] = max(dp[i], dp[i - k])
    
    ans = 0
    for i in range(maxn - 1, maxn - k - 1, -1):
        ans += dp[i]
    print(ans)


