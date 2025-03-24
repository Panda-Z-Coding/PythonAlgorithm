
#? 零钱兑换问题（Coin Change Problem）是动态规划领域的经典问题，
#? 其核心是用最少数量的硬币凑出指定金额

# 这也是一个完全背包问题

coins = [1, 2, 5]
amt = 11 # 要凑出的数
# dp[a] => 凑出金额a需要的最少硬币数
# 动态规划的非法状态初始化, dp[amt + 1] * (amt + 1)
# MAX = amt + 1 => 要凑出当前金额需要amt + 1个硬币，那是不可能的，所以就表示凑不到这个金额

def coin_change_dp_comp(coins, amt):
    MAX = amt + 1
    dp = [MAX] * MAX
    dp[0] = 0 # 凑金额0需要0个硬币
    
    for coin in coins:
        # 完全背包一维正序遍历
        for a in range(coin, MAX):
            dp[a] = min(dp[a], dp[a - coin] + 1)
            # dp[a] => 不选
            # dp[a-coin] + 1 => 选择
    print(*dp)
    return dp[amt] if dp[amt] != MAX else -1

# 如果要叫我们求解组合的方式
def coin_change_ii(coins, amt):
    '''计算组合数量'''
    dp = [0] * (amt + 1)
    dp[0] = 1 #! 注意凑出0元有一种选择方式
    
    for coin in coins:
        for a in range(coin, amt + 1):
            dp[a] += dp[a - coin]
    
    return dp[amt]

print(coin_change_dp_comp(coins, amt)) # 5 + 5 + 1