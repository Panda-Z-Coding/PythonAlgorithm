# dp[i][j][k] => (1, 1) -> (i, j) 一共向下走了k次的最大和
# 只需要向下走就可以确定一个状态
# 状态转移方程
# (i, j)可以从(i - 1, j)位置转移过来
# (i, j)可以从(i - 1, j - 1)位置转移过来
# dp[i][j][k] = max(dp[i-1][j][k-1], dp[i-1][j-1][k])
# 左右走次数相差不超过1
# 所以k最多取到 (n - 1) // 2 或者 (n - 1) // 2 + 1

# n - 1为奇数的时候对半分还有一个多余的可以给到向下或者右下
# n - 1是偶数的时候只能对半分, 也就是下面和右下次数一样

# 转移方程: dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[i][j]

# 最后走到的位置我们按照列来看的话就是中间附近
# 如果n是奇数的话, 中间我们怎么走, 到最后一行
# (n, (n - 1) // 2 + 1) or (n, (n - 1) // 2 + 1 + 1)
# 如果n是偶数的话
# (n, (n - 1) // 2 + 1)

# 打表

import os
import sys
input = sys.stdin.readline
# 
n = int(input())
dp = [list(map(int, input().split())) for i in range(n)]
# 初始化dp

for i in range(n): # 遍历每一行
    for j in range(i + 1): # 遍历每一列
        if i == 0: # 第一行
            dp[i][j] = dp[i][j] #? 为什么要加这个
        elif j == 0: # 如果不加 i == 0判断会从j == 0这里执行, 这样逻辑就有问题了, 每次只能执行一行
            dp[i][j] += dp[i-1][j] # 从上面走下来
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

if (n - 1) % 2 == 0: #? 
    # n-1是偶数 => n-1表示向下走的步数
    print(dp[n - 1][n // 2]) # 注意下标位置
else:
    print(max(dp[n - 1][n // 2], dp[n - 1][n // 2 - 1]))

# if n % 2 == 0:
#     print(max(dp[n - 1][n // 2 - 1],dp[n - 1][n // 2]))
# else:
#     print(dp[n - 1][n // 2])



