"""
重叠子问题、最优子结构
求解子问题
最优子问题: 子问题的最优解能否推出原问题的最优解
"""

#? 走楼梯-- 方案数
# 要走到n级台阶, 要么从n-1走一步, 要么从n-2走两步

#! dp[n] = dp[n-1] + dp[n-2]
# dp[1] = 1
# dp[2] = 2

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])

#! 变形

# 1. 每次可以上1,2,4阶
dp1 = [0] * (n+1)
dp1[1], dp1[2], dp1[3] = 1, 2, 5
for i in range(4, n + 1):
    dp1[i] = dp1[i-1] + dp1[i-2] + dp1[i-4]
print(dp1[n])

# 2. 每次上1, k
dp2 = [0] * (n + 1)
k = int(input())
for i in range(k):
    dp2[i] = 1
for i in range(k, n + 1):
    dp2[i] = dp2[i-1] + dp2[i-k]
print(dp2[n])

# 3. 每次上1,2,3...,k台阶
# dp3 = [0] * (n + 1)
# dp3[0] = 1
# sum3 = [0] * (n + 1)
# sum3[0] = dp3[0]
# for i in range(1, n + 1):
#     sum3[i] = sum3[i-1] + dp3[i]

# if n >= k:
#     print(sum3[n] - sum3[n - k - 1])
# else:
#     print(sum3[n])

'''
- 拆分子问题: 将问题拆解子问题, 找到问题之间的联系
- 确定状态
- 状态转移方程: 
- 实现
'''

#? 例子
# 1. 3367

# 2. 3423
