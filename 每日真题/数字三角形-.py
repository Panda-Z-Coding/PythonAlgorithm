n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# 自底向上动态规划
dp = [[0]*n for _ in range(n)]
dp[-1] = triangle[-1].copy()  # 最后一行初始化

for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

# 处理路径限制：当n为奇数时只能走到中间，偶数时可以走到中间两个
if n % 2 == 1:
    print(dp[0][0])
else:
    print(max(dp[0][0], dp[0][1]))
