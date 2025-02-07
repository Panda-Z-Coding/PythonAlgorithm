n, m, k = map(int, input().split())
mp = []
for i in range(n):
    mp.append(list(input()))
    
'''
dp[i][j][u][d] -> 表示位置在(i, j)经历u次方向变换的方向是d的方案数
d = 0 向下
d = 1 向右
'''
    
dp = [[[[0] * 2 for _ in range(k + 1)]for _ in range(m + 1)]for _ in range(n + 1)]

# 初始化
for i in range(n):
    if mp[i][0] != '#': 
        dp[i][0][0][0] = 1
    else:
        break

for j in range(m):
    if mp[0][j] != '#':
        dp[0][j][0][1] = 1 #! 你 TM! 能不能看清楚点这个是竖着走的！！
    else:
        break

# 遍历所有情况
for i in range(1, n):
    for j in range(1, m):
        if mp[i][j] != '#':
            for u in range(k + 1):
                # 原本方向过来的
                dp[i][j][u][0] = dp[i-1][j][u][0]
                dp[i][j][u][1] = dp[i][j-1][u][1]
                if u >= 1:
                    dp[i][j][u][0] += dp[i-1][j][u-1][1]
                    dp[i][j][u][1] += dp[i][j-1][u-1][0]
ans = 0
for u in range(k + 1):
    for d in range(2):
        ans += dp[n-1][m-1][u][d]
        
print(ans)