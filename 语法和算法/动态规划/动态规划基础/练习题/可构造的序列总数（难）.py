k, n = map(int, input().split())
mod = 10**9 + 7
max_num = 2000  # 假设k的最大值为2000

# 初始化DP数组：dp[i][j]表示长度为i，以j结尾的序列数
dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
for j in range(1, max_num + 1):
    dp[1][j] = 1  # 长度为1的序列每个j单独构成
for i in range(1, max_num + 1):
    dp[i][1] = 1  # 全1序列唯一

# 辅助函数：获取num的所有因数（去重）
def get_factors(num):
    factors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors

# 递推填充DP表
for i in range(2, n + 1):
    for j in range(2, k + 1):
        factors = get_factors(j)
        for factor in factors:
            dp[i][j] += dp[i-1][factor] #! 将j的因数作为元素插入序列的最后一位！
            dp[i][j] %= mod  # 取模防止溢出

# 计算结果：所有长度为n的序列之和
ans = sum(dp[n][j] for j in range(1, k + 1)) % mod
print(ans)