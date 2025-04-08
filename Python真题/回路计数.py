# 状态压缩dp
# dp[i][j] => 表示当前状态为i, 最后走到j这栋楼

# dp[i+ 1 << k][k] += dp[i][j] -> 从j走到k
# j,k 之间存在路径


import math
dp = [[0] * 22 for i in range(2100000)]
g = [[0] * 22 for i in range(22)] # 存储地图
n = 1 << 21
for i in range(1, 22):
    for j in range(1, 22):
        if math.gcd(i, j) == 1:
            g[i - 1][j - 1] = g[j - 1][i - 1] = 1
dp[1][0] = 1 # 从1教学楼开始
i = 1 # 表示状态
while i < n:
    for j in range(0, 21):
        if (i >> j & 1) == 0:
            # 没有访问过
            # 因为我dp定义是最后走到j
            continue
        for k in range(0, 21):
            if g[j][k] == 0 or (i >> k & 1) != 0:
                # i和k之间没有走廊
                # k教学楼访问过，就跳过
                continue
            dp[i + (1 << k)][k] += dp[i][j]
    i += 1
res= 0
for i in range(0, 21):
    res += dp[n - 1][i]
    # n - 1
print(res)
            





            
